from dataclasses import dataclass
@dataclass
class Player:
    first_name: str
    last_name: str
    position: str
    bats: int
    hits: int

def playerName(self):
    return f'{self.first_name} {self.last_name}'

def battingAvg
    avg = (self.hits/self.bats)
    return avg