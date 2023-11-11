from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from typing import Optional


def calculate_team_total_rating(players: Optional[list[Player]]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: Optional[list[Elf]]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Optional[list[Dwarf]]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
