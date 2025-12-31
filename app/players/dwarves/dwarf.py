from abc import ABC

from app.main import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the {self._hummer_level} level"
        )

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname}"
                f" with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
