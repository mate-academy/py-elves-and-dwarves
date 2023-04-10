from typing import Union
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: Union[list | Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: Union[list | Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Union[list | Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
