from app.players.player import Player


class Dwarf(Player):

    def __init__(self, favourite_dish):
        self._favorite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favorite_dish}")

