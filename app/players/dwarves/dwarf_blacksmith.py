from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, skill_level: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.__skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} "
                f"with skill of the {self.__skill_level} level")

    def get_rating(self) -> int:
        return self.__skill_level
