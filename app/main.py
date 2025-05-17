from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nick_name: str) -> None:
        self.nickname = nick_name

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):
    def __init__(self, nick_name: str,
                 musical_instrument: str) -> None:
        super().__init__(nick_name)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a "
              f"song on the {self._musical_instrument}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class Dwarf(Player):
    def __init__(self, nick_name: str,
                 favourite_dish: str) -> None:
        super().__init__(nick_name)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass

# Finally, create four classes: ElfRanger, Druid, DwarfWarrior and DwarfBlacksmith.

class ElfRanger(Elf):
    def __init__(self, nick_name: str,
                 musical_instrument: str,
                 bow_level: str) -> None:

        super().__init__(nick_name, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> None:
        print(f"Elf ranger {self.nickname}. "
              f"{self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(self, nick_name: str,
                 musical_instrument: str,
                 favourite_spell: str) -> None:

        super().__init__(nick_name, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> None:
        print(f"Druid {self.nickname}. "
              f"{self.nickname} has a favourite spell: {self._favourite_spell}")

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(self, nick_name: str,
                 favourite_dish: str,
                 hummer_level : int) -> None:

        super().__init__(nick_name, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> None:
        print(f"Dwarf warrior {self.nickname}. "
              f"{self.nickname} has a hummer of the {self._hummer_level} level")

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(self, nick_name: str,
                 favourite_dish: str,
                 skill_level : int) -> None:
        super().__init__(nick_name, favourite_dish)
        self._skill_level = skill_level

    def player_info(self) -> None:
        print(f"Dwarf blacksmith {self.nickname}. "
              f"{self.nickname} with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level