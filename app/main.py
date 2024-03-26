from typing import List, Union
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[Union[Elf]]) -> None:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Union[Dwarf]]) -> None:
    for dwarf in dwarves:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
