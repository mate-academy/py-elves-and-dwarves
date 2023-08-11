from app.elves.elf_ranger import ElfRanger
from app.elves.druid import Druid
from app.dwarves.dwarf_warrior import DwarfWarrior
from app.dwarves.dwarf_blacksmith import DwarfBlacksmith


elf_ranger = ElfRanger
druid = Druid
dwarf_warrior = DwarfWarrior
dwarf_blacksmith = DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    total = sum(player.rating for player in players)
    return total


def elves_concert(elf: list, play_elf_song: list) -> None:
    for elfs in elf:
        elfs.play_song(play_elf_song)


def feast_of_the_dwarves(dwarf: list, eat_favourite_dish: list) -> None:
    for dwarfs in dwarf:
        dwarfs.favourite_dish(eat_favourite_dish)
