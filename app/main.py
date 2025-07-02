from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str) -> None:
        self.nickname = name

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):
    def __init__(self, name: str, musical_instrument: str) -> None:
        super().__init__(name)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is"
              f"playing a song on the {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, name: str, favourite_dish: str) -> None:
        super().__init__(name)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(self, name: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(name, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}."
                f"{self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, name: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(name, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}."
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, name: str,
                 favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}."
                f"{self.nickname} has a hummer of the"
                f"{self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, name: str,
                 favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(name, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname}"
                f"with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
