from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):

    def __init__(self, **kwargs) -> None:
        nickname = kwargs.get("nickname")
        favourite_dish = kwargs.get("favourite_dish")
        skill_level = kwargs.get("skill_level")
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        result = str(f"Dwarf blacksmith {self.nickname} with")
        result += str(f" skill of the {self._skill_level} level")
        return result

    def get_rating(self) -> int:
        return self._skill_level
