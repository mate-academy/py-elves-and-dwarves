#from abc import ABC, abstractmethod

# class Player(ABC):
#     def __init__(self, nickname: str) -> None:
#         self.nickname = nickname
#     @abstractmethod
#     def get_rating(self):
#         pass
#
#     @abstractmethod
#     def player_info(self):
#         pass


# class Elf(Player):
#     def __init__(self, nickname: str, musical_instrument: str) -> None:
#         super().__init__(nickname)
#         self._musical_instrument = musical_instrument
#
#     def play_elf_song(self) -> None:
#         print(f"{self.nickname} is playing a song on the {self._musical_instrument}")


# class Dwarf(Player):
#     def __init__(self, nickname: str, favourite_dish: str) -> None:
#         super().__init__(nickname)
#         self._favourite_dish = favourite_dish
#
#     def eat_favourite_dish(self) -> None:
#         print(f"{self.nickname} is eating {self._favourite_dish}")

    # def player_info(self):
    #     return (f"Elf ranger {self.nickname}. "
    #             f"{self.nickname} has bow of the {self._bow_level} level")


# class ElfRanger(Elf):
#     def __init__(self, nickname: str, musical_instrument: str, bow_level: int) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._bow_level = bow_level
#
#     def player_info(self):
#         return (f"Elf ranger {self.nickname}. "
#                 f"{self.nickname} has bow of the {self._bow_level} level")
#
#     def get_rating(self) -> int:
#         return self._bow_level*3

# class Druid(Elf):
#     def __init__(self, nickname: str, musical_instrument: str, favourite_spell: str) -> None:
#         super().__init__(nickname, musical_instrument)
#         self._favourite_spell = favourite_spell
#
#     def get_rating(self) -> int:
#         return len(self._favourite_spell)
#
#     def player_info(self):
#         return (f"Druid {self.nickname}. "
#                 f"{self.nickname} has a favourite spell: {self._favourite_spell}")


# class DwarfWarrior(Dwarf):
#     def __init__(self, nickname: str, favourite_dish: str, hummer_level: int) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._hummer_level = hummer_level
#
#     def player_info(self):
#         return (f"Dwarf warrior {self.nickname}. "
#                 f"{self.nickname} has a hummer of the {self._hummer_level} level")
#
#     def get_rating(self) -> int:
#         return self._hummer_level + 4

# class DwarfBlacksmith(Dwarf):
#     def __init__(self, nickname: str, favourite_dish: str, skill_level: int) -> None:
#         super().__init__(nickname, favourite_dish)
#         self._skill_level = skill_level
#
#     def player_info(self):
#         return (f"Dwarf blacksmith {self.nickname} "
#                 f"with skill of the {self._skill_level} level")
#
#     def get_rating(self) -> int:
#         return self._skill_level

def calculate_team_total_rating(team: list[Player]) -> int:
    team_total_rating = 0
    return sum(player.get_rating() for player in team)

def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


ranger = ElfRanger(
    nickname="Nardual Chaekian",
    musical_instrument="flute",
    bow_level=7
)
print(ranger.get_rating())# == 21
print(ranger.player_info()) # == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute"

warrior = DwarfWarrior(
    nickname="Thiddeal",
    favourite_dish="French Fries",
    hummer_level=7
)
print(warrior.get_rating()) #== 11
print(warrior.player_info()) #== "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries"

team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
print(calculate_team_total_rating(team))

elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ElfRanger(nickname="Nardual Chaekian", musical_instrument="flute", bow_level=7)
]
elves_concert(elves)

dwarves = [
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries",hummer_level=7),
]
feast_of_the_dwarves(dwarves)
