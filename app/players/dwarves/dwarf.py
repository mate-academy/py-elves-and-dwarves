from app.players import player


class Dwarf(player.Player):
    def __init__(self, favourite_dish: str, nickname: str):
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")
