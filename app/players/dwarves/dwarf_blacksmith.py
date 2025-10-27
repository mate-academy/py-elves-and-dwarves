from app.dwarves.dwarf import Dwarf

class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, power: int, hammer_power: int):
        super().__init__(nickname, power)
        self.hammer_power = hammer_power

    def get_rating(self) -> int:
        return self.power + self.hammer_power

    def player_info(self) -> str:
        return f"{self.nickname} is Dwarf Blacksmith with rating {self.get_rating()}"
