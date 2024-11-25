from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for member in team:
        if isinstance(member, (ElfRanger, Druid,
                               DwarfWarrior, DwarfBlacksmith)):
            total_rating += member.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        if isinstance(elf, (ElfRanger, Druid)):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        if isinstance(dwarf, (DwarfWarrior, DwarfBlacksmith)):
            dwarf.eat_favourite_dish()
