from app.players.player import Player


class Dwarf(Player):

    def __init__(self, favorite_dish: str, nickname:str) -> None:
        super().__init__(nickname)
        self._favorite_dish = favorite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favorite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass
