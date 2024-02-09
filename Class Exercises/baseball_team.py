from dataclasses import dataclass
@dataclass
class Player:
    first_name: str
    last_name: str
    position: str
    at_bats: int
    hits: int

    def player_name(self):
        return f"{self.first_name} {self.last_name}"

    def batting_avg(self):
        avg = (self.hits/self.at_bats)
        return avg
