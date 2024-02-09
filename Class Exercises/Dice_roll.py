
import random

from dataclasses import dataclass
@dataclass

class Die:
    value: int

        def roll(self):
            self.value = random.randrange(1,7)



class Dice:
    value2: list =[]

