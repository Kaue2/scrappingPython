import seleniumHtml
from bs4 import BeautifulSoup
from product import Product
import json

url = "https://www.terabyteshop.com.br/"
page = seleniumHtml.htmlpage(url)
prods = []

doc = BeautifulSoup(page.htmlContent, 'html.parser')
products_contents = doc.findAll("div", {"class":"product-item__content"})

# try catch
for i in range(len(products_contents)):
    product_info = products_contents[i].findAll(name=["div", "a"], class_=lambda c : c in ["product-item__name", "product-item__new-price"])

    print(product_info)

    if len(product_info) >= 1:
        prod = Product(product_info[0].getText(), product_info[1].getText())
        prods.append(prod)

for i in range(len(prods)):
    print("Name: %s" % (prods[i].name))
    print("Preço: %f" % (prods[i].price))

jsonTeste = json.dumps([prod.serializeProd() for prod in prods], indent=4)

with open("jsonProducts.json", "w", encoding="utf-8") as file:
    file.write(jsonTeste)

print(jsonTeste)