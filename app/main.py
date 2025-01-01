from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior

def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for member in team:
        total_rating += member.get_rating()
    return total_rating

def elves_concert(team_elf: list) -> None:
    for member in team_elf:
        member.play_elf_song()

def feast_of_the_dwarves(team_dwarf: list) -> None:
    for member in team_dwarf:
        member.eat_favourite_dish()

# dwarves = [
#     DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
# ]
# feast_of_the_dwarves(dwarves)
#
# elves = [
#     Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
#     ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
# ]
# elves_concert(elves)
#
# team = [
#     Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
#     ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
# ]
# print(calculate_team_total_rating(team))