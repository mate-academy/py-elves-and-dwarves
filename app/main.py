from typing import List
from app.players.player import Player


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[str]) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[str]) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
