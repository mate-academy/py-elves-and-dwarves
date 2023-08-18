from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        skill_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        return "Dwarf blacksmith {0} with skill of the {1} level".format(
            self.nickname,
            self._skill_level
        )

    def get_rating(self) -> None:
        return self._skill_level
