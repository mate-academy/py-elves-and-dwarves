from app.players.players import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        self.__favourite_dish = favourite_dish
        super().__init__(nickname)

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.__favourite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass
