from dataclasses import dataclass

@dataclass
class Person:
    first_name: str
    last_name:str
    email: str

#WHats the difference between property and method

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

@dataclass
class Customer(Person):
    customer_number: str

@dataclass
class Employee(Person):
    SSN: int




def main():
    while True:
        customer = Customer(first_name="", last_name="", email="",customer_number="")
        employee = Employee(first_name="", last_name="", email="",SSN=0)
        print("Customer/Employee Date Entry")
        print()
        choice = input("Customer or employee? (c/e): ")
        if choice.lower() == "c":
            print()
            print("DATA ENTRY")
            customer.full_name = input("First name: ")
            customer.last_name = input("Last name: ")
            customer.email = input("Email: ")
            customer.customer_number = input("Number: ")
            print()
            print("CUSTOMER")
            print(f"Name: {customer.full_name}")
            print(f"Email: {customer.email}")
            print(f"Number: {customer.customer_number}")
        elif choice.lower() == "e":
            print()
            print("DATA ENTRY")
            employee.full_name = input("First name: ")
            employee.last_name = input("Last name: ")
            employee.email = input("Email: ")
            employee.SSN = input("Number: ")
            print()
            print("EMPLOYEE")
            print(f"Name: {employee.full_name}")
            print(f"Email: {employee.email}")
            print(f"SSN: {employee.SSN}")
        else:
            print("Invalid Choice. Try again.")
        print()
        again = input("Continue? (y/n): ")
        if again.lower() == "y":
            continue
        elif again.lower() == "n":
            break
    print()
    print("Bye!")

if __name__ == "__main__":
    main()