from typing import List

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(group: List[Elf]) -> List[None]:
    return [singer.play_elf_song() for singer in group]


def feast_of_the_dwarves(menu: List[Dwarf]) -> List[None]:
    return [dish.eat_favourite_dish() for dish in menu]
