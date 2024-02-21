from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    length: int
    __is_square: bool = False
    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return 2 * self.width + self.length

    @property
    def is_square(self):
        if self.length == self.width:
            return True
        else:
            return False