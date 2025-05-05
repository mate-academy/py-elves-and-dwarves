from app.players import Player


class Dwarf(Player):
    def __init__(self, _favourite_dish: str) -> None:
        self._favourite_dish = _favourite_dish

    def eat_favourite_dish(self) -> str:
        print(f"{self.nickname} is eating {self._favourite_dish}")
