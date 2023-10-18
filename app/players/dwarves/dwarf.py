from app.players.player import Player


class Dwarf(Player):
    def __init__(self, _favourite_dish: str) -> None:
        super().__init__()
        self._favourite_dish = _favourite_dish

    def eat_favourite_dish(self) -> None:
        return f"{self.nickname} is eating {self._favourite_dish}"
