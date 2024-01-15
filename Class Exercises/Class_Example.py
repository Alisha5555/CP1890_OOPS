
from Product_Example import Product



product1 = Product("Standley Hammer", 9.99,5)
product2 = Product("Quartet Marker",2.00,4)

print("Product Data ")
print(f"product1.name:\t\t {product1.name}")
print(f"Product Price:\t\t {product1.price:.2f}")
print(f"Discount Percent:\t\t {product1.discountPercent:d}%")

print(f"Discount Amount:\t\t {product1.getDiscountAmount():.2f}")
print(f"Discount Price:\t\t {product1.getDiscountPrice():.2f}")
