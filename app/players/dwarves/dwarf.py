from app.players.player import Player


class Dwarf(Player):
    def __init__(self, favourite_dish: int) -> str:
        self._favourite_dish = favourite_dish
    def eat_favourite_dish(self, nickname):
        print(f'{nickname} їсть {self._favourite_dish}')

