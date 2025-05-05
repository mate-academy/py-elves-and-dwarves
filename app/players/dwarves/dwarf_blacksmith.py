from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, _skill_level: str) -> None:
        super().__init__(nickname, _skill_level)
        self._skill_level = _skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname}."
            f"{self.nickname} with skill of the {self._skill_level}"
        )
