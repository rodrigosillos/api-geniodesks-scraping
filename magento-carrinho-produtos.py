#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import json
import sys
import requests

options = Options()
# options.add_argument("headless")
# options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://admin.geniodesks.signashop.com.br/painel")

campo_email = driver.find_element(By.NAME, "login[username]")
campo_email.send_keys("fernando@geniodesks.com.br")

campo_senha = driver.find_element(By.NAME, "login[password]")
campo_senha.send_keys("raFb148*SignaShopGd")

botao_entrar = driver.find_element(By.CLASS_NAME, 'form-button')
botao_entrar.send_keys(Keys.RETURN)

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//li//a//span[text()="Carrinho"]'))
driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//li//a//span[text()="Carrinhos abandonados"]'))
# driver.execute_script("arguments[0].click();", driver.find_element(By.ID, 'report_shopcart_export_button'))

# link = driver.find_element(By.XPATH, "//tbody/tr[@title]")
# python3 selenium-abandoned-car.py linha contato

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//tbody/tr[@title][' + sys.argv[1] + ']'))

time.sleep(10)

table_MN = pd.read_html(driver.page_source, attrs = {'id': 'customer_cart_grid1_table'})
json_data = json.loads(table_MN[0].to_json(orient="split"))

payload = {"contact": {'fieldValues': []}}

arr_fields = [[39,25,26], [27,28,29], [30,40,32], [33,42,41], [36,43,44]]

group = 0
field = 0

for lead in json_data['data']:
    produto_id = lead[0]
    produto_nome = lead[1]
    
    produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/m/e/mesa_com_regulagem_de_altura_geniodesk_pro.jpg'

    if produto_id == 338:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/g/e/geniodesk_plus.jpg'
    elif produto_id == 429:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/c/a/cadeira_geniodesk.jpg'
    elif produto_id == 406:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/v/e/veertebra-para-gerenciamento-de-cabos-3_2.jpg'
    elif produto_id == 395:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/c/a/calha_para_gerenciamento_de_cabos_1.jpg'
    elif produto_id == 337:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/m/e/mesa_com_regulagem_de_altura_geniodesk_pro.jpg'
    elif produto_id == 209:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/g/e/geniodesk_home.jpg'
    elif produto_id == 396:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/t/a/tapete-anti-fadiga.jpg'
    elif produto_id == 223:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/s/u/suporte-de-monitor-articulado-pistao-gas.jpg'  
    elif produto_id == 468:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/b/u/bundle_kit_1_-_geniodesks.jpg'
    elif produto_id == 234:
        produto_imagem = 'https://admin.geniodesks.signashop.com.br/media/catalog/product/s/u/suporte_de_cpu_geniodesks_1.jpg'                                      

    produto_preco = lead[4]

    payload["contact"]["fieldValues"].append({"field": arr_fields[group][field], 'value': produto_nome})
    field+=1

    payload["contact"]["fieldValues"].append({"field": arr_fields[group][field], 'value': produto_imagem})
    field+=1

    payload["contact"]["fieldValues"].append({"field": arr_fields[group][field], 'value': produto_preco})
    group+=1
    field=0

url = "https://geniodesks.api-us1.com/api/3/contacts/" + sys.argv[2]

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Api-Token": "e05c6ff73816579c31f23c5e1c86de782c50c9c2164c2906e1c0d08cf04b3e4ad4829551"
}

response = requests.put(url, json=payload, headers=headers)

driver.close()
