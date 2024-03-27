from dataclasses import dataclass
@dataclass
class Player:
    first_name: str = ""
    last_name: str = ""
    position: str = ""
    at_bats: int = 0
    hits: int = 0

    def player_name(self):
        return f"{self.first_name} {self.last_name}"

    def batting_avg(self):
        try:

            avg = (self.hits/self.at_bats)
            return avg
        except ZeroDivisionError:
            return 0.0

@dataclass
class Lineup:
    __player_list: list

    @property
    def count(self):
        return len(self.__player_list)

    def add_player(self, player: Player):
        self.__player_list.append(player)

    def print_lineup(self):
        for player in self.__player_list:
            print(f"{player.player_name()}")

    def remove_player(self, number):
        self.__player_list.pop(number - 1)

    def __iter__(self):
        for player in self.__player_list:
            yield player

def main():
    POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')
    lineup = Lineup([])
    lineup.add_player(Player("Arun","Rameshbabu","s",100,100))
    lineup.add_player(Player("Buster","Posey","C",4575,1380))

    for player in lineup:
        print(f"Player: {player.player_name()}")
        print(f"batting_avg: {player.batting_avg()}")
        print(f"Hits: {player.batting_avg()}")


if __name__ == "__main__":
    main()