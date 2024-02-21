from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float = 0.0
    discountPercent: int = 0

    def getDiscountAmount(self) -> float:
        return self.price - self.discountPercent

    def getDescription(self) -> str:
        return self.name


#@dataclass
#class Book(Product):
 #   author: str = " "
#
 #   def getDescription(self) -> str:
  #      return f"{Product.getDescription(self)} by {self.author}"


product1 = Product("Quartet Marker", 2.99, 20)
#book1 = Book("The Shining", 12.00, 10, 'Stephen King')

print(product1.getDescription())
#print(book1.getDescription())


@dataclass
class Movie(Product):
    movieyear: int = 0
    def getDescription(self) -> str:
        return f"{Product.getDescription(self)} year {self.movieyear}"

movie1 = Movie("Venom",4.99, 10, 2013)

print(movie1.getDescription())

class Book(Product):
    def __init__(self,name="",price=0.0,discountPercent=0,author=""):
        Product.__init__(self,name, price, discountPercent)
        self.author = author
book1 = Book("The Shining", 12.00, 10, 'Stephen King')
print(book1)


print(isinstance(movie1, Movie))
print(isinstance(movie1, Product))
print(isinstance(movie1, Book))

items =[book1, product1, movie1]
for item in items:
    if isinstance(item, Movie):
        print(item.getDescription)