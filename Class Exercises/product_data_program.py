from product_data import Product, Movie, Book

def title():
    print("PRODUCT DATA")


def main():
    book1 = Book("The Shining", 12.00, 10, 'Stephen King')
    product1 = Product("Quartet Marker", 2.99, 20)
    movie1 = Movie("Venom", 4.99, 10, 2013)
    items = [book1, product1, movie1]
    for item in items:
        if isinstance(item, Movie):
            print(f"Name: {item.getproductdiscription()}")
            print(f"Price {item.price}")
            print(f"Discount price {item.getdiscountprice()}")
        elif isinstance(item, Book):
            print(f"Name {item.name}")
            print(f"Price {item.price}")
            print(f"Discount price {item.getdiscountprice()}")
        elif isinstance(item, Product):
            print(f"Name: {item.getproductdiscription()}")
            print(f"Price {item.price}")
            print(f"Discount price {item.getdiscountprice()}")

main()