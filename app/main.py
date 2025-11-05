from abc import ABC, abstractmethod
from typing import List
import sys

# Емуляція структури пакетів для тестів
sys.modules["app.players.player"] = sys.modules[__name__]
sys.modules["app.players.elves.elf"] = sys.modules[__name__]
sys.modules["app.players.elves.elf_ranger"] = sys.modules[__name__]
sys.modules["app.players.elves.druid"] = sys.modules[__name__]
sys.modules["app.players.dwarves.dwarf"] = sys.modules[__name__]
sys.modules["app.players.dwarves.dwarf_warrior"] = sys.modules[__name__]
sys.modules["app.players.dwarves.dwarf_blacksmith"] = sys.modules[__name__]
sys.modules["app.main"] = sys.modules[__name__]


class Player(ABC):
    """Abstract base class for all players."""

    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Return player description."""
        pass


class Elf(Player):
    """Represents an elf with a musical instrument."""

    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument: str = musical_instrument

    def play_elf_song(self) -> None:
        print(
            f"{self.nickname} is playing a song "
            f"on the {self._musical_instrument}"
        )


class Dwarf(Player):
    """Represents a dwarf with a favourite dish."""

    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish: str = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")


class ElfRanger(Elf):
    """Represents an elf ranger with a bow."""

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        bow_level: int,
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level: int = bow_level

    def get_rating(self) -> int:
        return 3 * self._bow_level

    def player_info(self) -> str:
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the "
            f"{self._bow_level} level"
        )


class Druid(Elf):
    """Represents a druid with a favourite spell."""

    def __init__(
        self,
        nickname: str,
        musical_instrument: str,
        favourite_spell: str,
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell: str = favourite_spell

    def get_rating(self) -> int:
        return len(self._favourite_spell)

    def player_info(self) -> str:
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: "
            f"{self._favourite_spell}"
        )


class DwarfWarrior(Dwarf):
    """Represents a dwarf warrior with a hummer."""

    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        hummer_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._hummer_level: int = hummer_level

    def get_rating(self) -> int:
        return self._hummer_level + 4

    def player_info(self) -> str:
        return (
            f"Dwarf warrior {self.nickname}. "
            f"{self.nickname} has a hummer of the "
            f"{self._hummer_level} level"
        )


class DwarfBlacksmith(Dwarf):
    """Represents a dwarf blacksmith with skill level."""

    def __init__(
        self,
        nickname: str,
        favourite_dish: str,
        skill_level: int,
    ) -> None:
        super().__init__(nickname, favourite_dish)
        self._skill_level: int = skill_level

    def get_rating(self) -> int:
        return self._skill_level

    def player_info(self) -> str:
        return (
            f"Dwarf blacksmith {self.nickname} "
            f"with skill of the {self._skill_level} level"
        )


def calculate_team_total_rating(team: List[Player]) -> int:
    """Calculate the total rating of a player team."""
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    """Make all elves play their songs."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    """Make all dwarves eat their favourite dishes."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
