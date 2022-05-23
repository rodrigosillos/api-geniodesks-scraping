import pandas as pd

import requests
import json

hed = {
    'Host': 'admin.geniodesks.signashop.com.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': 'adminhtml=okm7aov3qr2rh9i3tsckml2bqt; X-Store=1; _BEAMER_USER_ID_TyUhCZkT5208=be9751f2-ea47-4cab-af69-dee77fe5da6f; _BEAMER_FIRST_VISIT_TyUhCZkT5208=2022-05-20T13:49:42.519Z; _BEAMER_LAST_POST_SHOWN_TyUhCZkT5208=null; _BEAMER_DATE_TyUhCZkT5208=2022-05-20T13:49:42.800Z; signashop_news_sidebar=1; _ga=GA1.3.855274881.1653054583; _gid=GA1.3.485232625.1653054583; frontend=ire9rkcmjjkl9fqd9slras7sre; mailchimp_landing_page=https%3A//admin.geniodesks.signashop.com.br/; _gcl_au=1.1.968973464.1653054857; _fbp=fb.2.1653054857837.1191215823; _gat=1; _BEAMER_FILTER_BY_URL_TyUhCZkT5208=false',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
}

data = {}
# data = {'mostrar_contato' : 'on'}
url = 'https://admin.geniodesks.signashop.com.br/index.php/painel/report_shopcart/abandoned/key/906ec3f9a0404c99d000bea9a12a5d17/limit/200/form_key/ErxxJBXtBToEkVD7/'

r = requests.post(url, json=data, headers=hed)

# table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota', match='Election results from statewide races')
table_MN = pd.read_html(r.text)
# table_MN = pd.read_html(r.text)

df = table_MN[2]

result = df.to_json(orient="split")
parsed = json.loads(result)
print(json.dumps(parsed, indent=4))

# print(df.head())
# print(df.info())
# print(df['Status Cliente'])
