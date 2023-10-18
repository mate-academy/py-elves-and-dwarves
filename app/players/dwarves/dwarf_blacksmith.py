from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            _favourite_dish: str,
            _skill_level: int
    ) -> None:
        super().__init__(nickname, _favourite_dish)
        self._skill_level = _skill_level

    def player_info(self) -> str:
        return f"Dwarf blacksmith {self.nickname} \
            with skill of the {self._skill_level} level"

    def get_rating(self) -> None:
        return self._skill_level
