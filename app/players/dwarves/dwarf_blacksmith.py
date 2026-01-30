from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            favourite_dish: str,
            nickname: str,
            skill_level: int
    ) -> None:
        super().__init__(
            nickname,
            favourite_dish
        )
        self._skill_level = skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} with "
                f"skill of the {self._skill_level} level")

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname}"
              f" is eating {self._favourite_dish}")
