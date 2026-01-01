from app.players.dwarves import DwarfWarrior, DwarfBlacksmith
from app.players.elves import Druid, ElfRanger


def calculate_team_total_rating(
        team: list[Druid | ElfRanger | DwarfWarrior | DwarfBlacksmith]
) -> int:
    total_rating = 0
    for member in team:
        total_rating += member.get_rating()
    return total_rating


def elves_concert(
        elves: list[Druid | ElfRanger]
) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(
        dwarves: list[DwarfWarrior | DwarfBlacksmith]
) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
