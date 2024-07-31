# from abc import ABC, abstractmethod
#
#
# class Player(ABC):
#     def __init__(self, nickname: str) -> None:
#         self.nickname = nickname
#
#     @abstractmethod
#     def get_rating(self) -> int:
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
#     def play_elf_song(self):
#         print(
#             f"{self.nickname} is playing"
#             f" a song on the {self._musical_instrument}"
#         )
#
#
# class Dwarf(Player):
#     def __init__(self, nickname: str, favourite_dish: str) -> None:
#         super().__init__(nickname)
#         self._favourite_dish = favourite_dish
#
#     def eat_favourite_dish(self):
#         print(f"{self.nickname} is eating {self._favourite_dish}")
#
#
# class ElfRanger(Elf):
#     def __init__(
#             self,
#             bow_level: int,
#             nickname: str,
#             musical_instrument: str
#     ) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#     def get_rating(self) -> int:
#         return 3 * self._bow_level
#
#     def player_info(self) -> str:
#         return (f"Elf ranger {self.nickname}."
#                 f"{self.nickname} has bow of the {self._bow_level} level")
#
#
# class Druid(Elf):
#     def __init__(
#             self,
#             favourite_spell: str,
#             musical_instrument: str,
#             nickname: str
#     ) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._favourite_spell = favourite_spell
#
#     def get_rating(self) -> int:
#         return len(self._favourite_spell)
#
#     def player_info(self) -> str:
#         return (f"Druid {self.nickname}."
#                 f"{self.nickname} has a favourite spell:"
#                 f"{self._favourite_spell}")
#
#
# class DwarfWarrior(Dwarf):
#     def __init__(
#             self,
#             hummer_level: int,
#             nickname: str,
#             favourite_dish: str
#     ) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._hummer_level = hummer_level
#
#     def get_rating(self) -> int:
#         return self._hummer_level + 4
#
#     def player_info(self) -> str:
#         return (f"Dwarf warrior {self.nickname}."
#                 f"{self.nickname} has a hummer"
#                 f"of the {self._hummer_level} level")
#
#
# class DwarfBlacksmith(Dwarf):
#     def __init__(
#             self,
#             skill_level: int,
#             nickname: str,
#             favourite_dish: str
#     ) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._skill_level = skill_level
#
#     def get_rating(self) -> int:
#         return self._skill_level
#
#     def player_info(self) -> str:
#         return (f"Dwarf blacksmith {self.nickname} with skill"
#                 f"of the {self._skill_level} level")
#
#
# def calculate_team_total_rating(players: list[Player]) -> int:
#     return sum(player.get_rating() for player in players)
#
#
# def elves_concert(elves: list[Elf]) -> None:
#     for elf in elves:
#         elf.play_elf_song()
#
#
# def feast_of_the_dwarves(feast: list[Dwarf]) -> None:
#     for dwarf in feast:
#         dwarf.eat_favourite_dish()


from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(feast: list[Dwarf]) -> None:
    for dwarf in feast:
        dwarf.eat_favourite_dish()
