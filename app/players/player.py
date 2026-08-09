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


from app.players.elves.elf import Elf  # noqa: E402, F401
from app.players.elves.druid import Druid  # noqa: E402, F401
from app.players.elves.elf_ranger import ElfRanger  # noqa: E402, F401
from app.players.dwarves.dwarf import Dwarf  # noqa: E402, F401
from app.players.dwarves.dwarf_warrior import DwarfWarrior  # noqa: E402, F401
from app.players.dwarves.dwarf_blacksmith import (  # noqa: E402, F401
    DwarfBlacksmith,
)
