from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str,
                 skill_level: int) -> None:
        """

        :type skill_level: object
        """
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def eat_favourite_dish(self) -> str:
        return (f"{self.nickname} "
                f"is eating {self.favourite_dish}")

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname}"
                f" with skill of the {self.skill_level} level")

    def get_rating(self) -> int:
        return self.skill_level
