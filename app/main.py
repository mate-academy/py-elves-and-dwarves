from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player
from typing import List


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(musicians: List[Elf]) -> List:
    concert = [musician.play_elf_song() for musician in musicians]
    return concert


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> List:
    feast = [dwarf.eat_favourite_dish() for dwarf in dwarves]
    return feast
