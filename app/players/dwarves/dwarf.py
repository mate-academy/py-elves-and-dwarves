from app.players.player import Player


class Dwarf(Player):
    # Why don't the tests
    # throw errors if I haven't
    # specified the abstract methods get_rating and player_info?
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.__favorite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.__favorite_dish}")
