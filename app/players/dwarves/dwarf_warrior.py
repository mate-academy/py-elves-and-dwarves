from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self.hummer_level = hummer_level

    def get_rating(self) -> int:
        self.hummer_level += 4
        return self.hummer_level

    def print_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level")
