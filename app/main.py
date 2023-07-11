from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(work_player.get_rating() for work_player in players)


def elves_concert(elfs: List[Elf]) -> None:
    for work_elfs in elfs:
        work_elfs.play_elf_song()


def feast_of_the_dwarves(dwarfs: List[Dwarf]) -> None:
    for work_dwarves in dwarfs:
        work_dwarves.eat_favourite_dish()
