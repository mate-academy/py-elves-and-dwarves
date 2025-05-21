from abc import abstractmethod
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


class Player:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
       pass

    @abstractmethod
    def player_info(self) -> None:
        if isinstance(self, ElfRanger):
            print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level")
        if isinstance(self, Druid):
            print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}")
        if isinstance(self, DwarfWarrior):
            print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level")
        if isinstance(self, DwarfBlacksmith):
            print(f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level")
