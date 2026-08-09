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


from app.players.elves.elf import (  # noqa: E402, F401
    Elf,
    Druid,
    ElfRanger,
)
from app.players.dwarves.dwarf import (  # noqa: E402, F401
    Dwarf,
    DwarfWarrior,
    DwarfBlacksmith,
)
