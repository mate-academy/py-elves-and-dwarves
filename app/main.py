from typing import List
from app.players.player import Player
from app.players.dwarves import dwarf
from app.players.elves import elf


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elfs: List[elf]) -> None:
    for player_elf in elfs:
        player_elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[dwarf]) -> None:
    for player_dwarf in dwarves:
        player_dwarf.eat_favourite_dish()
