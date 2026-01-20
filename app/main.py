from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[Elf]) -> None:
    if not all(isinstance(elf, Elf) for elf in elves):
        raise TypeError("All elements in the list must be instances of Elf")

    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    if not all(isinstance(dwarf, Dwarf) for dwarf in dwarves):
        raise TypeError("All elements in the list must be instances of Dwarf")

    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
