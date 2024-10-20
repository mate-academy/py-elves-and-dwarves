from players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")

    def get_rating(self) -> int:
        return 0

    def player_info(self) -> str:
        return f"Dwarf: {self.nickname}"
