from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> int:
        pass


class Elf(Player, ABC):
    def __init__(self, musical_instrument: str) -> None:
        super().__init__()
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

class Dwarf(Player, ABC):
    def __init__(self, favourite_dish: str) -> None:
        super().__init__()
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf, ABC):
    def __init__(self, bow_level: int) -> None:
        super().__init__(self._musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf, ABC):
    def __init__(self, favourite_spell: str) -> None:
        super().__init__(self._musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        return length(self._favourite_spell)

    def player_info(self) -> None:
        print(f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}")


class DwarfWarrior(Dwarf, ABC):
    def __init__(self, hummer_level: int) -> None:
        super().__init__(self._favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf, ABC):
    def __init__(self, skill_level: int) -> None:
        super().__init__(self._favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
