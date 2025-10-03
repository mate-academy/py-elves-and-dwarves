from app.players.player import Player


class Dwarf(Player):
    def __init__(self,name: str, favourite_dish: str) -> None:
        super().__init__(name)
        self._favourite_dish = favourite_dish
    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
