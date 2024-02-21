from product_data import Product, Book, Movie

def get_products():
    return (Product("Stanley 12 ounce wood hammer",5.489,10),
            Movie("The Holy Grail - DVD", 5.3, 10))

def show_products(product):
    w=18
    print()
    print(f"{'Name':{w}} {product.name}")
    if isinstance(product, Book):
        print(f"{'Price':{w}} {product.author}")
    elif isinstance(product, Movie):
        print(f"{'Year':{w}} {product.year}")
    print(f"{'Discount price':{w}}{product.discount_price():.2f}")
    print()


def main():
    test_products = get_products()
    for item in test_products:
        show_products(item)


main()