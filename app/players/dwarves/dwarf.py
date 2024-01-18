from app.players.player import Player


class Dwarf(Player):
    def __init__(self, favourite_dish: str, nickname: str) -> None:
        self._favourite_dish = favourite_dish
        self.nickname = nickname

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
