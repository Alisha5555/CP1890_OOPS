from dataclasses import dataclass

@dataclass
class Product:
    name: str= ""
    price: float = 0
    discountprice: int = 0

    def getdiscountprice(self):
        return self.price - self.discountprice
    def getproductdiscription(self):
        return self.name
@dataclass
class Movie(Product):
    year: int = 0

@dataclass
class Book(Product):
    author: str = ""