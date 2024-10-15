from app.players.player import Player


class Dwarf(Player):
    dwarves = []

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish
        Dwarf.dwarves.append(self)

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
