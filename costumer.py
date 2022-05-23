import pandas as pd

import requests
import json

hed = {
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Content-Length': '25',
	'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'adminhtml=okm7aov3qr2rh9i3tsckml2bqt; X-Store=1; _BEAMER_USER_ID_TyUhCZkT5208=be9751f2-ea47-4cab-af69-dee77fe5da6f; _BEAMER_FIRST_VISIT_TyUhCZkT5208=2022-05-20T13:49:42.519Z; _BEAMER_LAST_POST_SHOWN_TyUhCZkT5208=null; _BEAMER_DATE_TyUhCZkT5208=2022-05-20T13:49:42.800Z; signashop_news_sidebar=1; _ga=GA1.3.855274881.1653054583; _gid=GA1.3.485232625.1653054583; frontend=ire9rkcmjjkl9fqd9slras7sre; mailchimp_landing_page=https%3A//admin.geniodesks.signashop.com.br/; _gcl_au=1.1.968973464.1653054857; _fbp=fb.2.1653054857837.1191215823; _BEAMER_FILTER_BY_URL_TyUhCZkT5208=false; _gat=1',
    'Host': 'admin.geniodesks.signashop.com.br',
    'Origin': 'https://admin.geniodesks.signashop.com.br',
    'Referer': 'https://admin.geniodesks.signashop.com.br/index.php/painel/customer/edit/id/12295/active_tab/cart/key/a8a01067dd8b59c392450c1dac1a513f/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Sec-Fetch-User': '?1',
    'X-Prototype-Version': '1.7',	
    'X-Requested-With': 'XMLHttpRequest',

    '_BEAMER_DATE_TyUhCZkT5208': '2022-05-20T13:49:42.800Z',
    '_BEAMER_FILTER_BY_URL_TyUhCZkT5208': 'false',
    '_BEAMER_FIRST_VISIT_TyUhCZkT5208': '2022-05-20T13:49:42.519Z',
    '_BEAMER_LAST_POST_SHOWN_TyUhCZkT5208': 'null',
    '_BEAMER_USER_ID_TyUhCZkT5208': 'be9751f2-ea47-4cab-af69-dee77fe5da6f',
    '_fbp': 'fb.2.1653054857837.1191215823',
    '_ga': 'GA1.3.855274881.1653054583',
    '_gat': '1',
    '_gcl_au': '1.1.968973464.1653054857',
    '_gid': 'GA1.3.485232625.1653054583',
    'adminhtml': 'okm7aov3qr2rh9i3tsckml2bqt',
    'frontend': 'ire9rkcmjjkl9fqd9slras7sre',
    'mailchimp_landing_page': 'https://admin.geniodesks.signashop.com.br/',
    'signashop_news_sidebar': '1',
    'X-Store': '1',
}

data = {}
data = {'form_key' : 'ErxxJBXtBToEkVD7'}
url = 'https://admin.geniodesks.signashop.com.br/index.php/painel/customer/carts/id/12295/active_tab/cart/key/ba451a075755a87b592b328d882b76ae/'

r = requests.post(url, json=data, headers=hed)

print(r.text)


# df = pd.read_html(r.text, attrs = {'id': 'customer_cart_grid1_table'})
# table_MN = pd.read_html(r.text)

# df = table_MN[2]

# result = df.to_json(orient="split")
# parsed = json.loads(result)
# print(json.dumps(parsed, indent=4))

# print(df.head())
# print(df.info())
# print(df['Status Cliente'])