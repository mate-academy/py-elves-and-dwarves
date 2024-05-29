from typing import List
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: List[Elf]) -> None:  # correct?
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: List[Dwarf]) -> None:  # correct?
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
