# meta universe
# players :
# 1. Elves - 1. ElfRanger 2. Druid
# 2. Dwarves - 1. DwarfWarrior 2. DwarfBlacksmith
#____________________________________________________________
# from players.player import Player
#
# from players.elves.elf import Elf
# from players.elves.elf_ranger import ElfRanger
# from players.elves.druid import Druid
#
# from players.dwarves.dwarf import Dwarf
# from players.dwarves.dwarf_warrior import DwarfWarrior
# from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
#____________________________________________________________




from players.player import Player

from players.elves.elf import Elf
from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid

from players.dwarves.dwarf import Dwarf
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith

# class Player(ABC):
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     @abstractmethod
#     def get_rating(self):
#         pass
#
#     @abstractmethod
#     def player_info(self):
#         pass
#
#     def testt(self):
#         print("TEST")
#
#
# class Elf(Player):
#     def __init__(self, nickname, musical_instrument):
#         super().__init__(nickname)
#         self._musical_instrument = musical_instrument
#
#     def play_elf_song(self):
#         print(f"{self.nickname} is playing a song"
#               f" on the {self._musical_instrument}")
#
#     def get_rating(self):
#         if isinstance(self, Elf):
#             if isinstance(self, ElfRanger):
#                 return self._bow_level * 3
#             else:
#                 return len(self._favourite_spell)
#
#     def player_info(self):
#         if isinstance(self, Elf):
#             if isinstance(self, ElfRanger):
#                 return (f"Elf ranger {self.nickname}. {self.nickname} has bow "
#                         f"of the {self._bow_level} level")
#             else:
#                 return (f"Druid {self.nickname}. {self.nickname} has a "
#                         f"favourite spell: {self._favourite_spell}")
#
#
# class Dwarf(Player):
#     def __init__(self, nickname, favourite_dish):
#         super().__init__(nickname)
#         self._favorite_dish = favourite_dish
#
#     def get_rating(self):
#         if isinstance(self, Dwarf):
#             if isinstance(self, DwarfWarrior):
#                 return self._hummer_level + 4
#             else:
#                 return self._skill_level
#
#     def player_info(self):
#         if isinstance(self, Dwarf):
#             if isinstance(self, DwarfWarrior):
#                 return (f"Dwarf warrior {self.nickname}. {self.nickname} has "
#                         f"a hummer of the {self._hummer_level} level")
#             else:
#                 return (f"Dwarf blacksmith {self.nickname} with skill of the "
#                         f"{self._skill_level} level")
#
#     def eat_favourite_dish(self):
#         print(f"{self.nickname} is eating {self._favorite_dish}")
#
#
# class ElfRanger(Elf):
#     def __init__(self, nickname, musical_instrument, bow_level: int):
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#
# class Druid(Elf):
#     def __init__(self, nickname, musical_instrument, favourite_spell: str):
#         super().__init__(nickname, musical_instrument)
#         self._favourite_spell = favourite_spell
#
#
# class DwarfWarrior(Dwarf):
#     def __init__(self, nickname, favourite_dish, hummer_level):
#         super().__init__(nickname, favourite_dish)
#         self._hummer_level = hummer_level
#
#
# class DwarfBlacksmith(Dwarf):
#     def __init__(self, nickname, favourite_dish, skill_level):
#         super().__init__(nickname, favourite_dish)
#         self._skill_level = skill_level



def calculate_team_total_rating(team):
    return sum(player.get_rating() for player in team)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()



# elf_test = Elf("Zhora elf", "Violin")
# elf_test.play_elf_song()
# dwarf_test = Dwarf("Stepa Korotkiy", "M'yaso")
# dwarf_test.eat_favourite_dish()
# elf_ranger_test = ElfRanger("Sanya", "Guitar", 32)
# print(elf_ranger_test.__dict__)
# dudu_test = Druid("Vasyl", "Sopilochka", "Leviossa")
# print(dudu_test.__dict__)
# korotish_war = DwarfWarrior("Kolya molot", "Pelmen's", 44)
# print(elf_ranger_test.player_info())
# print(dudu_test.player_info())
# korotish_craft = DwarfBlacksmith("Oleg Zavod", "Rul'ka", 9000)
# print(korotish_craft.player_info())
# print(korotish_war.get_rating())
# print(korotish_craft.get_rating())
# print(dudu_test.get_rating())
# print(elf_ranger_test.get_rating())
#
#
# ranger = ElfRanger(
#     nickname="Nardual Chaekian",
#     musical_instrument="flute",
#     bow_level=7
# )
# print(ranger.get_rating()) # 21
# print(ranger.player_info()) # #== "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
# ranger.play_elf_song() # "Nardual Chaekian is playing a song on the flute"
#
#
# warrior = DwarfWarrior(
#     nickname="Thiddeal",
#     favourite_dish="French Fries",
#     hummer_level=7
# )
# print(warrior.get_rating()) #  11
# print(warrior.player_info()) # "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
# warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries"
#
# team = [
#     Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
#     ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
# ]
# print(calculate_team_total_rating(team)) # 102
# elves = [
#     Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
#     ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
# ]
# elves_concert(elves)
#
#
# dwarves = [
#     DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
# ]
# feast_of_the_dwarves(dwarves)



# app/
#     main.py
#     players/
#         player.py
#         elves/
#             elf.py
#             elf_ranger.py
#             druid.py
#         dwarves/
#             dwarf.py
#             dwarf_warrior.py
#             dwarf_blacksmith.py