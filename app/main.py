from typing import List

from app.players.player import Player

from app.players.elves.elf import Elf

from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves_only: List[Elf]) -> str:
    for elf in elves_only:
        elf.play_elf_song()


def feast_of_the_dwarves(gnomy: List[Dwarf]) -> str:
    for dwarf in gnomy:
        dwarf.eat_favourite_dish()
