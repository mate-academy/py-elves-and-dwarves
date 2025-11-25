from abc import ABC, abstractmethod
from typing import List


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass


class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )


class ElfRanger(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        bow_level: int
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the "
            f"{self._bow_level} level"
        )

    def get_rating(self) -> int:
        return 3 * self._bow_level


class Druid(Elf):
    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: "
            f"{self._favourite_spell}"
        )

    def get_rating(self) -> int:
        return len(self._favourite_spell)


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(
            f"{self.nickname} is eating "
            f"{self._favourite_dish}"
        )


class DwarfWarrior(Dwarf):
    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level = hummer_level

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the "
            f"{self._hummer_level} level"
        )

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

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} with skill "
            f"of the {self._skill_level} level"
        )

    def get_rating(self) -> int:
        return self._skill_level


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    print(ranger.get_rating())
    print(ranger.player_info())
    ranger.play_elf_song()

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    print(warrior.get_rating())
    print(warrior.player_info())
    warrior.eat_favourite_dish()

    team = [
        Druid(
            nickname="Druid",
            musical_instrument="flute",
            favourite_spell="ABC"
        ),
        ElfRanger(
            nickname="Ranger",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]

    print(calculate_team_total_rating(team))

    elves = [
        Druid(
            nickname="Nardual",
            musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(
            nickname="Thiddeal",
            favourite_dish="French Fries",
            hummer_level=3
        ),
        DwarfWarrior(
            nickname="Dwarf",
            favourite_dish="Caesar Salad",
            hummer_level=3
        ),
    ]
    feast_of_the_dwarves(dwarves)
