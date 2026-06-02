from app.players.elves.elf_ranger import ElfRanger  # noqa: F401
from app.players.elves.druid import Druid  # noqa: F401
from app.players.dwarves.dwarf_warrior import DwarfWarrior  # noqa: F401
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith  # noqa: F401


def calculate_team_total_rating(team: list) -> int:
    counter = 0
    for player in team:
        counter += player.get_rating()
    return counter


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
