from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass


class Elf(Player):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(self, nickname: str, musical_instrument: str, bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level


class Druid(Elf):
    def __init__(self, nickname: str, musical_instrument: str, favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell


class DwarfWarrior(Dwarf):
    def __init__(self, nickname: str, musical_instrument: str, hummer_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._hummer_level = hummer_level

