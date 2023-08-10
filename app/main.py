from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


elf_ranger = ElfRanger
druid = Druid
dwarf_warrior = DwarfWarrior
dwarf_blacksmith = DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    total = sum(player.rating for player in players)
    return total


def elves_concert(play_elf_song: list) -> None:
    for elf in play_elf_song:
        elf.play_song(play_elf_song)


def feast_of_the_dwarves(eat_favourite_dish: list) -> None:
    for dwarf in eat_favourite_dish:
        dwarf.favourite_dish(eat_favourite_dish)
