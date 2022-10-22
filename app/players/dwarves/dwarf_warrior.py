from app.players.dwarves.dwarf import Dwarf


class DwarfWarrior(Dwarf):
    def __init__(self,
                 nickname: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4


if __name__ == "__main__":
    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7)

    print(warrior.get_rating())
# == 11
    print(warrior.player_info())
# == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
    print(warrior.eat_favourite_dish())
# "Thiddeal is eating French Fries"
