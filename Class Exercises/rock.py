from dataclasses import dataclass
import random

@dataclass
class Player:
    name: str
    value: str

    def generateRoshambo(self):
        value = "Rock"
        return value
    def play(self, ):





@dataclass
class Bart(Player):
    name = "Bart"


rps = ["Rock", "Paper", "Scissors"]


@dataclass
class Lisa(Player):
    name = "Lisa"

    def generateRoshambo(self):
        play = random.choice(rps)
        return play
