from testclass1 import Rectangle



def main():
    r1 = Rectangle(width=int(input("Enter width1:")), length=int(input("Enter length1:")))
    r2 = Rectangle(width=int(input("Enter width2:")), length=int(input("Enter length2:")))
    r3 = Rectangle(width=int(input("Enter width3:")), length=int(input("Enter length3:")))
    print()
    print(r1.area)
    print(r1.perimeter)
    print(r1.is_square)
    print()
    print(r2.area)
    print(r2.perimeter)
    print(r2.is_square)
    print()
    print(r3.area)
    print(r3.perimeter)
    print(r3.is_square)


main()