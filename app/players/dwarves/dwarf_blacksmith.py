from app.players.dwarves.dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str,
                 favourite_dish: str,
                 skill_level: int) -> str:
        self.nickname = nickname
        self.favourite_dish = favourite_dish
        self.skill_level = skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} with "
            f"skill of the {self.skill_level} level"
        )

    def get_rating(self) -> int:
        return self.skill_level

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
