from players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__()
        self._nickname = nickname
        self._favourite_dish = favourite_dish

    @property
    def nickname(self) -> None:
        return self._nickname

    def eat_favourite_dish(self) -> None:
        print(f"{self._nickname} is eating {self._favourite_dish}")
