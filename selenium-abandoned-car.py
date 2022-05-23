from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup
import pandas as pd
import json
import sys

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
# python3 selenium-abandoned-car.py 3

driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//tbody/tr[@title][' + sys.argv[1] + ']'))

time.sleep(5)

# print(driver.page_source)

table_MN = pd.read_html(driver.page_source, attrs = {'id': 'customer_cart_grid1_table'})
df = table_MN[0]
result = df.to_json(orient="split")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))

# soup_level1=BeautifulSoup(driver.page_source, 'lxml')
# table = soup_level1.find_all('table')[1]

# table_MN = pd.read_html(str(table), header=0)

# df = table_MN[0]

# result = df.to_json(orient="split")
# parsed = json.loads(result)
# print(json.dumps(parsed, indent=4))

# ID_Produto = driver.find_element(By.XPATH, '//tbody/tr/td[5]')
# print(ID_Produto.text)
# # print(ID_Produto.get_attribute("value"))

# time.sleep(15)

# driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//a[text()="Faturamento"]'))
# driver.find_element(By.ID, "frmFaturamento").submit()
# driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "invoicecheck"))
# driver.find_element(By.ID, "frmExcelFaturamento").submit()

driver.close()