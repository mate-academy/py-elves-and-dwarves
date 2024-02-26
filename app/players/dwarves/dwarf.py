from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname, favourite_dish):
        super().__init__(nickname)
        self.__protected = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.__protected}")

    def get_rating(self):
        pass

    def player_info(self):
        pass
