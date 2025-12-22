from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: str
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def player_info(self) -> None:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self.skill_level} level")

    def get_rating(self) -> None:
        return self.skill_level
