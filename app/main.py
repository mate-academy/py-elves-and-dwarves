from abc import abstractmethod

class Player:
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass

class Elf(Player):
    def __init__(self, musical_instrument: str) -> None:
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song \
        on the {self._musical_instrument}")

class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")

class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> None:
        self._bow_level = bow_level


class Druid(Elf):
    def __init__(self, favourite_spell: str) -> None:
        self._favourite_spell = favourite_spell


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int) -> None:
        self._hummer_level = hummer_level


class DwarfBlacksmit(Dwarf):
    def __init__(self, skill_level: int) -> None:
        self._skill_level = skill_level

