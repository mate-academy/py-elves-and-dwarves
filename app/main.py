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

    def get_rating(self):
        pass

    def player_info(self):
        pass

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def get_rating(self):
        pass

    def player_info(self):
        pass

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self):
        return f"Elf ranger {self.nickname}." \
               f" {self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return self._bow_level * 3


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self):
        return f"Druid {self.nickname}." \
               f" {self.nickname} has a favourite spell: {self._favourite_spell}"

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class DwarfWarrior(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self):
        return f"Dwarf warrior {self.nickname}." \
               f" {self.nickname} has a hummer of the {self._hummer_level} level"

    def get_rating(self) -> int:
        return self._hummer_level + 4


class DwarfBlacksmith(Dwarf):
    def __init__(
            self,
            nickname: str,
            favourite_dish: str,
            skill_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level = skill_level

    def player_info(self):
        return f"Dwarf blacksmith {self.nickname}" \
               f" with skill of the {self._skill_level} level"

    def get_rating(self) -> int:
        return self._skill_level


def calculate_team_total_rating(team: list) -> int:
    return sum([teammate.get_rating() for teammate in team])


def elves_concert(elves: list) -> None:
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves]



