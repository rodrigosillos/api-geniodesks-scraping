#!/usr/bin/python3

import pandas as pd

import requests
import json
import time
import sys

hed = {
    'Host': 'admin.geniodesks.signashop.com.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': '_BEAMER_USER_ID_TyUhCZkT5208=be9751f2-ea47-4cab-af69-dee77fe5da6f; _BEAMER_FIRST_VISIT_TyUhCZkT5208=2022-05-20T13:49:42.519Z; _BEAMER_DATE_TyUhCZkT5208=2022-08-01T15:13:54.581Z; _ga=GA1.3.855274881.1653054583; _fbp=fb.2.1653054857837.1191215823; adminhtml=73gdmt2ou5namr3nfkah6l5bkn; X-Store=1; _gid=GA1.3.815718365.1660847966; _BEAMER_FILTER_BY_URL_TyUhCZkT5208=false',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Referer': '',

    '_BEAMER_DATE_TyUhCZkT5208':	'2022-08-01T15:13:54.581Z',
    '_BEAMER_FILTER_BY_URL_TyUhCZkT5208': 'false',
    '_BEAMER_FIRST_VISIT_TyUhCZkT5208': '2022-05-20T13:49:42.519Z',
    '_BEAMER_USER_ID_TyUhCZkT5208': 'be9751f2-ea47-4cab-af69-dee77fe5da6f',
    '_fbp': 'fb.2.1653054857837.1191215823',
    '_ga': 'GA1.3.855274881.1653054583',
    # '_gat':	'1',
    '_gcl_au': '1.1.968973464.1653054857',
    '_gid': 'GA1.3.755842421.1659969963',
    'adminhtml': '4hohc8es9einm9d81e37bsqu4i',
    # 'signashop_news_sidebar': '1',
    'X-Store': '1',
}

data = {}
url = 'https://admin.geniodesks.signashop.com.br/index.php/painel/report_shopcart/abandoned/key/65e43f367db62cbeb80a5cf3fc37514f/filter/Y3JlYXRlZF9hdCU1QmxvY2FsZSU1RD1wdF9CUiZ1cGRhdGVkX2F0JTVCbG9jYWxlJTVEPXB0X0JS/form_key/wfYQstHyqdZ2fzsM/'

r = requests.post(url, json=data, headers=hed)

table_MN = pd.read_html(r.text)
json_data = json.loads(table_MN[2].to_json(orient="split"))

linha = 1

for lead in json_data['data']:
    email = lead[1]

    url = "https://geniodesks.api-us1.com/api/3/contacts?email=" + email

    headers = {
        "Accept": "application/json",
        "api-token": "e05c6ff73816579c31f23c5e1c86de782c50c9c2164c2906e1c0d08cf04b3e4ad4829551"
    }

    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)

    if len(json_data['scoreValues']) > 0:
        contact = json_data['scoreValues'][0]['contact']
    else:
        contact = json_data['contacts'][0]['id']

    script_descriptor = open("magento_carrinho_produtos.py")
    a_script = script_descriptor.read()
    sys.argv = ["magento_carrinho_produtos.py", str(linha), contact]
    exec(a_script)
    
    linha+=1

    time.sleep(10)
