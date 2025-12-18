from typing import List
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> float:
    return sum(player.get_rating() for player in team)


def elves_concert(team: List[Elf]) -> None:
    for player in team:
        player.play_elf_song()


def feast_of_the_dwarves(team: List[Dwarf]) -> None:
    for player in team:
        player.eat_favourite_dish()
