from dataclasses import dataclass
@dataclass
class Customer:
    cust_id: int
    first_name: str
    last_name: str
    company_name:str
    address:str
    city:str
    state:str
    zip:str

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_address(self):
        if self.company_name == "":
            location = f"{self.address}\n{self.city}, {self.state} {self.zip}"
        else:
            location = f"{self.company_name}\n{self.address}\n{self.city}, {self.state} {self.zip}"
        return location


#TEST
#def main():
 #   person = Customer(id=1091, first_name="John", last_name="Doe", company="", address="123 road", city="New York", state="CA", zip="12345")
  #  print(person.full_name)
   # print(person.full_address)
#main()