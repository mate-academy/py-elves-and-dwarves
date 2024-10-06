from app.players.player import Player
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(rating.get_rating() for rating in team)


def elves_concert(elves) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()

# team = [
#     Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
#     ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
# ]

# print(calculate_team_total_rating(team))
# calculate_team_total_rating(team) == 102  # 33 * 3 + 3


# elves = [
#     Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
#     ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
# ]

# elves_concert(elves)
# "Nardual is playing a song on the flute"
# "Rothilion is playing a song on the trumpet"


# dwarves = [
#     DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
# ]

# feast_of_the_dwarves(dwarves)
# "Thiddeal is eating French Fries"
# "Dwarf is eating Caesar Salad"

#----------------------------------------------------------------

# ranger = ElfRanger(
#     nickname="Nardual Chaekian",
#     musical_instrument="flute",
#     bow_level=7
# )
#
# print(ranger.get_rating())
# print(ranger.player_info())
# print(ranger.play_elf_song())

# ranger.get_rating() == 21
# ranger.player_info() == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
# ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute"



# warrior = DwarfWarrior(
#     nickname="Thiddeal",
#     favourite_dish="French Fries",
#     hummer_level=7
# )
#
# print(warrior.get_rating())
# print(warrior.player_info())
# print(warrior.eat_favourite_dish())

# warrior.get_rating() == 11
# warrior.player_info() == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
# warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries"
