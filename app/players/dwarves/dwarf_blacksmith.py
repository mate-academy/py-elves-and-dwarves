from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            _favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(nickname)
        self._favourite_dish = _favourite_dish
        self._skill_level = skill_level

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname}"
                f" with skill of the"
                f" {self._skill_level} level")
