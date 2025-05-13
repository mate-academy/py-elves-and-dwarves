from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass


class Elf(Player):
    def __init__(self, musical_instrument: str) -> None:
        self.musical_instrument = musical_instrument

    @staticmethod
    def play_elf_song() -> None:
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        self.favourite_dish = favourite_dish

    @staticmethod
    def eat_favourite_dish() -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")

    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass


class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> None:
        self.bow_level = bow_level

    @abstractmethod
    def get_rating(self) -> str:
        return "3 * self.bow_level for ElfRanger"

    @abstractmethod
    def player_info(self) -> str:
        return "Elf ranger {self.nickname}. {self.nickname} has bow of the {self.bow_level} level"


class Druid(Elf):
    def __init__(self, favourite_spell: str) -> None:
        self.favorite_spell = favourite_spell

    @abstractmethod
    def get_rating(self) -> str:
        return "length of favourite_spell for Druid"

    @abstractmethod
    def player_info(self) -> str:
        return "Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"


class DwarfWarrior(Dwarf):
    def __init__(self, hummer_level: int) -> None:
        self.hummer_level = hummer_level

    @abstractmethod
    def get_rating(self) -> str:
        return "self.hummer_level + 4 for DwarfWarrior"

    def player_info(self) -> str:
        return "Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self.hummer_level} level"


class DwarfBlacksmith(Dwarf):
    def __init__(self, nickname: str, favourite_dish: str, skill_level: int):
        super().__init__(nickname, favourite_dish)
        self.skill_level = skill_level

    def get_rating(self) -> str:
        return "self.skill_level for DwarfBlacksmith"

    def player_info(self) -> str:
        return "Dwarf blacksmith {self.nickname} with skill of the {self.skill_level} level"


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)

def elves_concert(elves: list[Elf]):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
