from app.players.player import Player


class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def get_rating(self) -> str:
        return "NotImplemented"

    def player_info(self) -> str:
        return "NotImplemented"