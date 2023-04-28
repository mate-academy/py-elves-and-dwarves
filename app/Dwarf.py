

class Dwarf(Player):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str
    ) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return f"Dwarf warrior {self.nickname}. {self.nickname} " \
               f"has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return 4 + self._hummer_level


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(nickname=nickname, favourite_dish=favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} with skill of the " \
               f"{self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level