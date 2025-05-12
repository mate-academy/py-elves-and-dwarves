from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.__favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.__favourite_dish}")
