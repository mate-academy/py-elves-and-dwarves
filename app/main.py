from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, nickname) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> str:
        if self is ElfRanger:
            return 3 * self.bow_level

    @abstractmethod
    def player_info(self) -> str:
            if self is ElfRanger:
                return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"
            if self is Druid:
                return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level"
            if self is DwarfWarrior:
                return f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"
            if self is DwarfBlacksmith:
                return f"Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"


class Elf(Player):
    def __init__(self, nickname, musical_instrument) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, favourite_dish) -> None:
        super().__init__(favourite_dish)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(self, name, musical_instrument, bow_level: int) -> None:
        super().__init__(name, musical_instrument)
        self._bow_level = bow_level


class Druid(Elf):
    def __init__(self, name, musical_instrument, favourite_spell) -> None:
        super().__init__(name, musical_instrument)
        self._favourite_spell = favourite_spell


class DwarfWarrior(Dwarf):
    def __init__(self, name, favourite_dish, hummer_level) -> None:
        super().__init__(name, favourite_dish)
        self._hummer_level = hummer_level


class DwarfBlacksmith(Dwarf):
    def __init__(self, name, favourite_dish, skill_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._skill_level = skill_level
