from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


# noqa: E402
from app.players.elves.elf import Elf  # noqa: F401
from app.players.elves.druid import Druid  # noqa: F401
from app.players.elves.elf_ranger import ElfRanger  # noqa: F401
from app.players.dwarves.dwarf import Dwarf  # noqa: F401
from app.players.dwarves.dwarf_warrior import DwarfWarrior  # noqa: F401
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith  # noqa: F401
