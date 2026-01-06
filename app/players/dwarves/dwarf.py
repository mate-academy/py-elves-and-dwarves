from app.player import Player


class Dwarf(Player):
    def __init__(self, nickname, favorite_dish):
        super().__init__(nickname)
        self._favorite_dish = favorite_dish


    def eat_favorite_dish(self):
        print(f"{self.nicckname} is eating {self.favorite_dish}")