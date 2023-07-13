from app.players import player


class Dwarf(player.Player):
    def __init__(self, nickname: str,
                 favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(
            f"{self.nickname} is "
            f"eating {self._favourite_dish}"
        )
