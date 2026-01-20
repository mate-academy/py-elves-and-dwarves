from .players.player import Player
from .players.dwarves.dwarf import Dwarf
from .players.elves.elf import Elf


# Write following functions:
# * `calculate_team_total_rating` -
# it should take list of `Player`s and
# return the sum of the ratings for all team members
# ```python
# team = [
#     Druid(nickname="Druid",
#     musical_instrument="flute", favourite_spell="ABC"),
#     ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
# ]
# calculate_team_total_rating(team) == 102  # 33 * 3 + 3


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)

# * `elves_concert` - it should take a list
# of `Elf` and call `play_elf_song` method for each elf.
# ```python
# elves = [
#     Druid(nickname="Nardual",
#     musical_instrument="flute", favourite_spell="aaa"),
#     ElfRanger(nickname="Rothilion",
#     musical_instrument="trumpet", bow_level=33),
# ]
# elves_concert(elves)
# # "Nardual is playing a song on the flute"
# # "Rothilion is playing a song on the trumpet"


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()

# * `feast_of_the_dwarves` - it should take a
# list of `Dwarf` and call `eat_favourite_dish` method for each dwarf.
# ```python
# dwarves = [
#     DwarfWarrior(nickname="Thiddeal",
#     favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf",
#     favourite_dish="Caesar Salad", hummer_level=3),
# ]
# feast_of_the_dwarves(dwarves)
# # "Thiddeal is eating French Fries"
# # "Dwarf is eating Caesar Salad"


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()

# Use the following project structure:
# ```
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
# ```
# All classes should be defined in the corresponding modules.
# Functions should be defined in the `main.py` module.
#
# ### Note: Check your code using this
# [checklist](checklist.md) before pushing your solution.
#
