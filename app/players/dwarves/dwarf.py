from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

        def eat_favorite_dish() -> None:
            print(f"{self.nickname} is eating {self._favourite_dish}")
