from app.players.dwarves.dwarf_warrior import DwarfWarrior, Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.druid import Elf, Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(team: list[Dwarf | Elf]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Druid | ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(
        dwarves: list[DwarfWarrior | DwarfBlacksmith]
) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
