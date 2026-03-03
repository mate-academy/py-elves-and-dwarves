from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from typing import List


def calculate_team_total_rating(
    team: List[Player]
) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(
    team: List[Elf]
) -> None:
    for elf in team:
        elf.play_elf_song()


def feast_of_the_dwarves(
    team: List[Dwarf]
) -> None:
    for dwarf in team:
        dwarf.eat_favourite_dish()
