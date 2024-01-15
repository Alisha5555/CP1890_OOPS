
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    discountPercent: int

    def getDiscountAmount(self):
        return self.price * (self.discountPercent / 100)

    def getDiscountprice(self):
        return self.price - self.getDiscountAmount()

product1 = Product("Standley 13 ounce wood Hammer", 9.99, 5)
product2 = Product("National Hardware 3/4''Wire Nails", 5.00, 4)
product3 = Product("Economy Duct Tape, 60 yds, Sliver",8.00, 5)

products = [product1, product2, product3]

def product_1():
    print("\nPRODUCT DATA")
    print(f"Name:\t\t\t\t {product1.name}")
    print(f"Price:\t\t\t\t {product1.price:.2f}")
    print(f"Discount Percent:\t {product1.discountPercent:d}%")
    print(f"Discount Amount:\t {product1.getDiscountAmount():.2f}")
    print(f"Discount Price:\t\t {product1.getDiscountprice():.2f}")
def product_2():
    print("\nPRODUCT DATA")
    print(f"Name:\t\t\t\t {product2.name}")
    print(f"Price:\t\t\t\t {product2.price:.2f}")
    print(f"Discount Percent:\t {product2.discountPercent:d}%")
    print(f"Discount Amount:\t {product2.getDiscountAmount():.2f}")
    print(f"Discount Price:\t\t {product2.getDiscountprice():.2f}")
def product_3():
    print("\nPRODUCT DATA")
    print(f"Name:\t\t\t\t {product3.name}")
    print(f"Price:\t\t\t\t {product3.price:.2f}")
    print(f"Discount percent:\t {product3.discountPercent:d}%")
    print(f"Discount amount:\t {product3.getDiscountAmount():.2f}")
    print(f"Discount price:\t\t {product3.getDiscountprice():.2f}")
def main():
    print("The Product Viewer program\n")
    print("PRODUCTS")
    for i, item in enumerate(products, start=1):
        print(f"{i}.\t{item.name}")
    while True:
        num = input("\nEnter product number: ")
        if num == "1":
            product_1()
        elif num == "2":
            product_2()
        elif num == "3":
            product_3()
        else:
            print("\nInvalid")
        again = input("\nView another product? (y/n): ")
        if again.lower() == "n":
            print("\nBye!")
            break










main()