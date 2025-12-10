from typing import List

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player

def calculate_team_total_rating(players: List[Player]):
    return sum(player.get_rating() for player in players)

def elves_concert(elves: List[Elf]):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: List[Dwarf]):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
