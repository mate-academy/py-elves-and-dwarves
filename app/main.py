from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf

# pprint.pprint(sys.path)
# class Player:
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


# class Elf(Player):
#     def __init__(self, nickname, musical_instrument):
#         super().__init__(nickname)
#         self._musical_instrument = musical_instrument
#     def play_elf_song(self):
#         print(f"{self.nickname} is playing a song on the {self._musical_instrument}")
#
#     def get_rating(self):
#         pass
#
#     def player_info(self):
#         pass
#
#
# class Dwarf(Player):
#     def __init__(self, nickname, favourite_dish):
#         super().__init__(nickname)
#         self._favourite_dish = favourite_dish
#     def eat_favourite_dish(self):
#         print(f"{self.nickname} is eating {self._favourite_dish}")
#
#     def get_rating(self):
#         pass
#
#     def player_info(self):
#         pass


# class ElfRanger(Elf):
#     def __init__(self, nickname, musical_instrument, bow_level: int):
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#     def get_rating(self):
#         return self._bow_level * 3
#
#     def player_info(self):
#         return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level"
#
#
# class Druid(Elf):
#     def __init__(self, nickname, musical_instrument, favourite_spell: str):
#         super().__init__(nickname, musical_instrument)
#         self._favourite_spell = favourite_spell
#
#     def get_rating(self):
#         return len(self._favourite_spell)
#
#     def player_info(self):
#         return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self._favourite_spell}"
#
#
#
# class DwarfWarrior(Dwarf):
#
#     def __init__(self, nickname, favourite_dish, hummer_level: int):
#         super().__init__(nickname, favourite_dish)
#         self._hummer_level = hummer_level
#
#     def get_rating(self):
#         return self._hummer_level + 4
#
#     def player_info(self):
#         return f"Dwarf warrior {self.nickname}. {self.nickname} has a hummer of the {self._hummer_level}"
#
#
# class DwarfBlacksmith(Dwarf):
#
#     def __init__(self, nickname, favourite_dish, skill_level: int):
#         super().__init__(nickname, favourite_dish)
#         self._skill_level = skill_level
#
#     def get_rating(self):
#         return self._skill_level
#
#     def player_info(self):
#         return f"Dwarf blacksmith {self.nickname} with skill of the {self._skill_level} level"


# ranger = ElfRanger(
#     nickname="Nardual Chaekian",
#     musical_instrument="flute",
#     bow_level=7
# )
# print(ranger.get_rating()) # 21
# print(ranger.player_info()) # "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
# print(ranger.play_elf_song())  # "Nardual Chaekian is playing a song on the flute"
# warrior = DwarfWarrior(
#     nickname="Thiddeal",
#     favourite_dish="French Fries",
#     hummer_level=7
# )
# print(warrior.get_rating()) # 11
# print(warrior.player_info()) # "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
# print(warrior.eat_favourite_dish())  # "Thiddeal is eating French Fries"
#
# team = [
#     Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
#     ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
# ]
#
# print(ranger.play_elf_song(), "1111111111")  # "Nardual Chaekian is playing a song on the flute"
def calculate_team_total_rating(team: list):
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating

# print(calculate_team_total_rating(team)) # 33 * 3 + 3

# elves = [
#     Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
#     ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
# ]
def elves_concert(elves):
    for elf_play in elves:
        elf_play.play_elf_song()

# elves_concert(elves)

# dwarves = [
#     DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
# ]
def feast_of_the_dwarves(dwarves):
    for dwarves_feast in dwarves:
        dwarves_feast.eat_favourite_dish()

# feast_of_the_dwarves(dwarves)
