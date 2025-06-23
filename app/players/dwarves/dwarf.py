from app.players.player import Player


class Dwarf(Player):

    def __init__(self,
                 nickname: str,
                 favourite_dish: str
                 ) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


def main() -> None:
    pass


if __name__ == "__main__":
    main()
