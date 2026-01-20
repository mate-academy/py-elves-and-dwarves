from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    @property
    def favourite_dish(self) -> str:
        return self._favourite_dish

    @favourite_dish .setter
    def favourite_dish(self, value: str) -> None:
        self._favourite_dish = value

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
