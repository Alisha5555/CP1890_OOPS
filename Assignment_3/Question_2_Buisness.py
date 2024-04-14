# Import the dataclass module for use in the program
from dataclasses import dataclass


# use the dataclass module to make a class to assign variables
@dataclass
class Player:
    name: str
    wins: int
    losses: int
    ties: int

    # create a module to add all the types of data together to return a total games variable
    def games(self):
        games = self.wins + self.losses + self.ties
        return games
