from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname


class Elves(Player):
    def __init__(self, nickname: str,  musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
class Dwarves(Player):


class ElfRanger(Elves):


class Druid(Elves):


class DwarfWarrior(Dwarves):


class DwarfBlacksmith(Dwarves):

