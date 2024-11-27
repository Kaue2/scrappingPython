import htmlPage
import seleniumHtml
from bs4 import BeautifulSoup
import re

url = "https://www.terabyteshop.com.br/"
page = htmlPage.requests(url)
page2 = seleniumHtml.htmlpage(url)


doc = BeautifulSoup(page2.htmlContent, 'html.parser')
products_contents = doc.findAll("div", {"class":"product-item__content"})
product_info = products_contents[0].findAll(name=["div", "a"], class_=lambda c : c in ["product-item__name", "product-item__new-price"])
content = product_info[0].getText()

print(content)

for i in range (len(product_info)):
    print("%s \n" % (product_info[i]))