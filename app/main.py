# from abc import ABC, abstractmethod
#
#
# class Player(ABC):
#     def __init__(self, nickname: str) -> None:
#         self.nickname = nickname
#
#     @abstractmethod
#     def get_rating(self) -> str:
#         pass
#
#     @abstractmethod
#     def player_info(self) -> str:
#         pass
#
#
# class Elf(Player):
#     def __init__(self, nickname: str, musical_instrument: str) -> None:
#         super().__init__(nickname)
#         self._musical_instrument = musical_instrument
#
#     def play_elf_song(self) -> str:
#         return (f"{self.nickname} is playing a song on the "
#                 f"{self._musical_instrument}")
#
#     def get_rating(self) -> str:
#         pass
#
#     def player_info(self) -> str:
#         pass
#
#
# class Dwarf(Player):
#     def __init__(self, nickname: str, favourite_dish: str) -> None:
#         super().__init__(nickname)
#         self._favourite_dish = favourite_dish
#
#     def eat_favourite_dish(self) -> str:
#         return f"{self.nickname} is eating {self._favourite_dish}"
#
#     def get_rating(self) -> str:
#         pass
#
#     def player_info(self) -> str:
#         pass
#
#
# class ElfRanger(Elf):
#     def __init__(self, nickname: str,
#                  musical_instrument: str,
#                  bow_level: int) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#     def player_info(self) -> str:
#         return (f"Elf ranger {self.nickname}. "
#                 f"{self.nickname} has bow of the {self._bow_level} level")
#
#     def get_rating(self) -> int:
#         return 3 * self._bow_level
#
#
# class Druid(Elf):
#     def __init__(self, nickname: str,
#                  musical_instrument: str,
#                  favourite_spell: str) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._favourite_spell = favourite_spell
#
#     def player_info(self) -> str:
#         return (f"Druid {self.nickname}. "
#                 f"{self.nickname} has a favourite spell: "
#                 f"{self._favourite_spell}")
#
#     def get_rating(self) -> int:
#         return len(self._favourite_spell)
#
#
# class DwarfWarrior(Dwarf):
#     def __init__(self, nickname: str,
#                  favourite_dish: str,
#                  hummer_level: int) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._hummer_level = hummer_level
#
#     def player_info(self) -> str:
#         return (f"Dwarf warrior {self.nickname}. "
#                 f"{self.nickname} has a hummer of the "
#                 f"{self._hummer_level} level")
#
#     def get_rating(self) -> int:
#         return self._hummer_level + 4
#
#
# class DwarfBlacksmith(Dwarf):
#     def __init__(self, nickname: str,
#                  favourite_dish: str,
#                  skill_level: int) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._skill_level = skill_level
#
#     def player_info(self) -> str:
#         return (f"Dwarf blacksmith {self.nickname} "
#                 f"with skill of the {self._skill_level} level")
#
#     def get_rating(self) -> int:
#         return self._skill_level
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([char.get_rating() for char in players])


def elves_concert(elvs_list: list[Elf]) -> None:
    [elf.play_elf_song() for elf in elvs_list]


def feast_of_the_dwarves(dwarvs_list: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarvs_list]
