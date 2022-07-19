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
    'Cookie': '_BEAMER_USER_ID_TyUhCZkT5208=be9751f2-ea47-4cab-af69-dee77fe5da6f; _BEAMER_FIRST_VISIT_TyUhCZkT5208=2022-05-20T13:49:42.519Z; _BEAMER_DATE_TyUhCZkT5208=2022-05-20T13:49:42.800Z; _ga=GA1.3.855274881.1653054583; _gcl_au=1.1.968973464.1653054857; _fbp=fb.2.1653054857837.1191215823; X-Store=1; adminhtml=6o1oo5pnhlt5u4u31jlfvb1adq; _gid=GA1.3.2069784406.1658152036',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Referer': 'https://admin.geniodesks.signashop.com.br/index.php/painel/report_shopcart/abandoned/key/21aa8d23a1a8e819a13a0ffa0d97cccb/filter/Y3JlYXRlZF9hdCU1QmxvY2FsZSU1RD1wdF9CUiZ1cGRhdGVkX2F0JTVCbG9jYWxlJTVEPXB0X0JS/form_key/J1JbkQTLV2nmJH7J/',

    'BEAMER_DATE_TyUhCZkT5208':	'2022-05-20T13:49:42.800Z',
    '_BEAMER_FILTER_BY_URL_TyUhCZkT5208': 'false',
    '_BEAMER_FIRST_VISIT_TyUhCZkT5208': '2022-05-20T13:49:42.519Z',
    '_BEAMER_USER_ID_TyUhCZkT5208': 'be9751f2-ea47-4cab-af69-dee77fe5da6f',
    '_fbp': 'fb.2.1653054857837.1191215823',
    '_ga': 'GA1.3.855274881.1653054583',
    '_gcl_au': '1.1.968973464.1653054857',
    '_gid': 'GA1.3.32295845.1657288887',
    'adminhtml': 'tc6j0qe7mh976fdp31vno48l4o',
    'X-Store': '1',
}

data = {}
url = 'https://admin.geniodesks.signashop.com.br/index.php/painel/report_shopcart/abandoned/key/206dd69adcd0993902f0677c1ace9962/filter/Y3JlYXRlZF9hdCU1QmxvY2FsZSU1RD1wdF9CUiZ1cGRhdGVkX2F0JTVCbG9jYWxlJTVEPXB0X0JS/form_key/B6XbFhfzfSGcrRzi/'

r = requests.post(url, json=data, headers=hed)

table_MN = pd.read_html(r.text)
json_data = json.loads(table_MN[2].to_json(orient="split"))

i = 1

for lead in json_data['data']:
    email = lead[1]

    url = "https://geniodesks.api-us1.com/api/3/contacts?email=" + email

    headers = {
        "Accept": "application/json",
        "api-token": "e05c6ff73816579c31f23c5e1c86de782c50c9c2164c2906e1c0d08cf04b3e4ad4829551"
    }

    response = requests.get(url, headers=headers)
    json_data = json.loads(response.text)

    contact = json_data['scoreValues'][0]['contact']

    script_descriptor = open("magento-carrinho-produtos.py")
    a_script = script_descriptor.read()
    sys.argv = ["magento-carrinho-produtos.py", str(i), contact]
    exec(a_script)
    
    i+=1

    time.sleep(10)