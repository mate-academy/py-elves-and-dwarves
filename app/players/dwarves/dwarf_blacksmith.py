from .dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            skill_level: int,
            favourite_dish: str | None = None
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self.skill_level} level"
        )

    def get_rating(self) -> int:
        return self.skill_level
