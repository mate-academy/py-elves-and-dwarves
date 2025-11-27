from abc import ABC, abstractmethod
from typing import List


class Player(ABC):

    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player, ABC):

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self.musical_instrument: str = musical_instrument

    @abstractmethod
    def play_elf_song(self) -> None:
        pass


class Dwarf(Player, ABC):

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self.favourite_dish: str = favourite_dish

    @abstractmethod
    def eat_favourite_dish(self) -> None:
        pass


class ElfRanger(Elf):

    def __init__(self, nickname: str, musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self.bow_level: int = bow_level

    def get_rating(self) -> int:
        return self.bow_level * 3

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
            f"{self.bow_level} level"
        )

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song on the "
            f"{self.musical_instrument}"
        )


class Druid(Elf):

    def __init__(self, nickname: str, musical_instrument: str,
                 favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self.favourite_spell: str = favourite_spell

    def get_rating(self) -> int:
        return len(self.favourite_spell) + 2

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. {self.nickname} has a favourite spell: "
            f"{self.favourite_spell}"
        )

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song on the "
            f"{self.musical_instrument}"
        )


class DwarfWarrior(Dwarf):

    def __init__(self, nickname: str, favourite_dish: str,
                 hummer_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.hummer_level: int = hummer_level

    def get_rating(self) -> int:
        return self.hummer_level + 5

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of "
            f"the {self.hummer_level} level"
        )

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")


class DwarfBlacksmith(Dwarf):

    def __init__(self, nickname: str, favourite_dish: str,
                 skill_level: int) -> None:
        super().__init__(nickname, favourite_dish)
        self.skill_level: int = skill_level

    def get_rating(self) -> int:
        return self.skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} with skill of the "
            f"{self.skill_level} level"
        )

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
