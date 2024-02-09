from dataclasses import dataclass
@dataclass
class Product:
    name:str
    __price:float
    discountPercent:int


    def getDiscountAmount(self):
        return self.__price * (self.discountPercent / 100)

    def getDiscountprice(self):
        return self.__price - self.getDiscountAmount()

    @property
    def show_price(self):
        return int(self.__price)







