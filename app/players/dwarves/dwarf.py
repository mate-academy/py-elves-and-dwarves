from ..players import Player


class Dwarf(Player):

    def __init__(self, nickname: str, favorite_dish: str) -> None:
        super().__init__(nickname)
        self._favorite_dish = favorite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favorite_dish}")
