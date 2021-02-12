import requests
from bs4 import BeautifulSoup
import json

# function finding all gategory links
def find_all_links(link, headers, tag, class_name):
    responce = requests.get(link, headers=headers).text
    soup = BeautifulSoup(responce, 'lxml')
    nav_bar = soup.find(tag, class_=class_name)
    items = nav_bar.find_all('a')
    return items


#function for printing all product name and prices
def product_parser(product_list, atr, name, price ):
    for item in product_list:
        data = item.get(atr)
        product = json.loads(data)
        print(f"Product Name: {product[name]}, ProductPriceInclTax: {product[price]}")
