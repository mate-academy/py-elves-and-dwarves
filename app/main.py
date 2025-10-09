from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elves(Player):
    def __init__(self, musical_instrument: str) -> None:
        super().__init__(self.nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing "
              f"a song on the {self._musical_instrument}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class Dwarves(Player):
    def __init__(self, favourite_dish: str) -> None:
        super().__init__(self.nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating "
              f"{self._favourite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class ElfRanger(Elves):
    def __init__(self, bow_level: int) -> None:
        super().__init__(self.nickname)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elves):
    def __init__(self, favourite_spell: str) -> None:
        super().__init__(self.nickname)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite "
                f"spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarves):
    def __init__(self, hummer_level: int) -> None:
        super().__init__(self.nickname)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (f"Dwarf warrior {self.nickname}. "
                f"{self.nickname} has a hummer of "
                f"the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarves):
    def __init__(self, skill_level: int) -> None:
        super().__init__(self.nickname)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname} with "
                f"skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level
