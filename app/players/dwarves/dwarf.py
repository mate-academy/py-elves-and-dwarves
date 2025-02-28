from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish: str = favourite_dish

    def eat_favourite_dish(self) -> str:
        print(
            f"{self.nickname} is eating "
            f"{self._favourite_dish}"
        )
