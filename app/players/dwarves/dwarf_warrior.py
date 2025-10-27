from app.dwarves.dwarf import Dwarf

class DwarfWarrior(Dwarf):
    def get_rating(self) -> int:
        return self.power * 3

    def player_info(self) -> str:
        return f"{self.nickname} is Dwarf Warrior with rating {self.get_rating()}"
