import requests
from bs4 import BeautifulSoup
import json

def extract_products(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    for product in soup.select('.vtex-product-summary-2-x-nameContainer'):
        name = product.select_one('..vtex-product-summary-2-x-productBrand').text.strip()
        price = product.select_one('.product-price .tiendasjumboqaio-jumbo-minicart-2-x-price').text.strip()
        products.append({'name': name, 'price': price})
    return products

url = 'https://www.tiendasjumbo.co/supermercado'
products = extract_products(url)

data = {'url': url, 'products': products}
json_data = json.dumps(data)

print(json_data)

