from app.players import player


class Dwarf(player.Player):
    def __init__(self, nickname, favourite_dish):
        self._favourite_dish = favourite_dish
        super().__init__(nickname)

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
