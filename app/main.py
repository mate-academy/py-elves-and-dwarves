from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: list) -> int:
    rating_sum_team = 0
    for teammate in team:
        rating_sum_team += teammate.get_rating()
    return rating_sum_team


def elves_concert(team: list) -> None:
    for teammate in team:
        teammate.play_elf_song()


def feast_of_the_dwarves(team: list) -> None:
    for teammate in team:
        teammate.eat_favourite_dish()
