from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, hummer_level: int, favourite_dish: str) -> str:
        self._hummer_level = hummer_level
        self.nickname = nickname
        self.favourite_dish = favourite_dish

    def player_info(self):
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level")

    def get_rating(self):
        print(self._hummer_level + 4)

    def eat_favourite_dish(self):
        print(f"{self.nickname}. {self.nickname} is eating {self.favourite_dish}")

#warrior = DwarfWarrior(
#    nickname="Thiddeal",
#    favourite_dish="French Fries",
#    hummer_level=7
#)
#warrior.get_rating() #== 11
#warrior.player_info() #== "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
#warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries"
