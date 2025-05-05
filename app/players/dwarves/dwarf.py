from players.player import Player


class Dwarf(Player):
    def __init__(self, _favourite_dish: str, nickname: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = _favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
