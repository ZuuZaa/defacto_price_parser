import requests
from bs4 import BeautifulSoup
from headers import headers
from helper_def import find_all_links, product_parser

link = 'https://www.defacto.com.tr'
# all categories
items = find_all_links(link, headers,'nav','mainmenu')
# all products
for a in items:
    href = a.get('href')
    category_responce = requests.get(f'{link}/{href}').text
    soup = BeautifulSoup(category_responce, 'lxml')
    product_list = soup.find_all('div', class_='products-card')
    product_parser(product_list, 'data-documents', 'ProductName', 'ProductPriceInclTax')





