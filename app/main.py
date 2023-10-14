from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[Elf]) -> list:
    return [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> list:
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
