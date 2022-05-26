# from abc import ABC, abstractmethod
# from app.players.dwarves.dwarf import Dwarf
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
#
# from app.players.elves.elf import Elf
# from app.players.elves.elf_ranger import ElfRanger
# from app.players.elves.druid import Druid


def calculate_team_total_rating(players: list):
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
