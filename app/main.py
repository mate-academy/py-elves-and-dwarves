# Старий чорновий код — залишено для подальшого аналізу.
#
# from abc import ABC, abstractmethod
#
#
# class Player(ABC):
#     def __init__(self, nickname: str) -> None:
#         self.nickname = nickname
#
#     @abstractmethod
#     def get_rating(self) -> None:
#         pass
#
#     @abstractmethod
#     def player_info(self) -> None:
#         pass
#
#     @abstractmethod
#     def declared(self) -> None:
#         pass
#
#
# class Elf(Player):
#     def __init__(self, nickname: str, musical_instrument) -> None:
#         super().__init__(nickname)
#         self._musical_instrument = musical_instrument
#
#     def play_elf_song(self) -> None:
#         print(
#             f"{self.nickname} is playing a song "
#             f"on the {self._musical_instrument}"
#         )
#
#
# class ElfRanger(Elf):
#     def __init__(
#             self, nickname: str, musical_instrument, bow_level
#     ) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#     def player_info(self) -> str:
#         return (
#             f"Elf ranger {self.nickname}. {self.nickname} "
#             f"has bow of the {self._bow_level} level"
#         )
#
#     def get_rating(self) -> None:
#         return 3 * self._bow_level
#
#
# class Druid(Elf):
#     def __init__(
#             self, nickname, musical_instrument, favourite_spell: str
#     ) -> None:
#         super
#         self._favourite_spell = favourite_spell
#
#     def player_info(self) -> str:
#         return (
#             f"Druid {self.nickname}. {self.nickname} has a "
#             f"favourite spell: {self._favourite_spell}"
#         )
#
#     def get_rating(self) -> int:
#         return len(self._favourite_spell)
#
#
# class Dwarf(Player):
#     def __init__(self, nickname: str, favourite_dish) -> None:
#         super().__init__(nickname)
#         self._favourite_dish = favourite_dish
#
#     def eat_favourite_dish(self) -> None:
#         print(
#             f"{self.nickname} is playing a song "
#             f"on the {self._favourite_dish}"
#         )
#
#
# class DwarfWarrior(Dwarf):
#     def __init__(self, hummer_level: int) -> None:
#         super().__init__(hummer_level)
#         self._hummer_level = hummer_level
#
#     def player_info(self) -> str:
#         return (
#             f"Dwarf warrior {self.nickname}. {self.nickname} "
#             f"has a hummer of the {self._hummer_level} level"
#         )
#
#     def get_rating(self) -> int:
#         return self._hummer_level + 4
#
#
# class DwarfBlacksmith(Dwarf):
#     def __init__(self, skill_level: int) -> None:
#         super().__init__(skill_level)
#         self._skill_level = skill_level
#
#     def player_info(self) -> str:
#         return (
#             f"Dwarf blacksmith {self.nickname} with skill "
#             f"of the {self._skill_level} level"
#         )
#
#     def get_rating(self) -> int:
#         return self._skill_level
#
#
# def calculate_team_total_rating()

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
