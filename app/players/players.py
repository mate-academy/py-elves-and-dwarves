from abc import ABC, abstractmethod
from players.elves.elf_ranger import ElfRanger


class Player(ABC):
    def __init__(self, nickname) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass