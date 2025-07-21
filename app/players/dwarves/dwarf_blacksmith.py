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

    def get_rating(self) -> float:
        pass

    def player_info(self) -> dict:
        pass
