from app.players import Player
class Dwarf(Player):

    def __init__(self, nickname, favourite_dish) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish
