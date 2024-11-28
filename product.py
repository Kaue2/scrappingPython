import re

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = ''
        self.treatPrice(price)

    def treatPrice(self, price) -> None:
        price = re.sub(r'[^\d,]', '', price)
        self.price = float(re.sub(r',', '.', price))

    def serializeProd(self):
        return{
            "name" : self.name,
            "price" : self.price
        }