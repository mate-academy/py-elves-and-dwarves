from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(
        team: list[ElfRanger, Druid, DwarfWarrior, DwarfBlacksmith]
) -> int:
    return sum(person.get_rating() for person in team)


def elves_concert(team: list[ElfRanger | Druid]) -> None:
    for person in team:
        if isinstance(person, (Druid, ElfRanger)):
            person.play_elf_song()
        continue


def feast_of_the_dwarves(team: list[DwarfWarrior | DwarfBlacksmith]) -> None:
    for person in team:
        if isinstance(person, (DwarfBlacksmith, DwarfWarrior)):
            person.eat_favourite_dish()
        continue
