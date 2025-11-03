from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(el.get_rating() for el in players_list)


def elves_concert(elves: list[Elf]) -> str:
    return [el.play_elf_song() for el in elves]


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> str:
    return [el.eat_favourite_dish() for el in dwarves]
