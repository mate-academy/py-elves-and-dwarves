from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def player_info(self) -> str:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass


from app.players.elves.elf import Elf  # noqa: E402
from app.players.elves.elf_ranger import ElfRanger  # noqa: E402
from app.players.elves.druid import Druid  # noqa: E402
from app.players.dwarves.dwarf import Dwarf  # noqa: E402
from app.players.dwarves.dwarf_warrior import DwarfWarrior  # noqa: E402
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith  # noqa: E402


__all__ = [
    "Player",
    "Elf",
    "ElfRanger",
    "Druid",
    "Dwarf",
    "DwarfWarrior",
    "DwarfBlacksmith",
]
