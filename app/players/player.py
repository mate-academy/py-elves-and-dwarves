# flake8: noqa: E402

from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


# Re-eksport klas, których oczekują testy
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid

from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


__all__ = [
    "Player",
    "Elf",
    "ElfRanger",
    "Druid",
    "Dwarf",
    "DwarfWarrior",
    "DwarfBlacksmith",
]
