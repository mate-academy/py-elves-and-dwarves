from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int, ) -> str:
        self.nickname = nickname
        self.favourite_dish = favourite_dish
        self.hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self.hummer_level} level"

    def get_rating(self) -> int:
        return self.hummer_level + 4

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating "
              f"{self.favourite_dish}")
