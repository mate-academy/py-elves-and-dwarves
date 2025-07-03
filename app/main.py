from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player

def calculate_team_total_rating(players_list: list) -> int:
    total_rating = 0
    for player in players_list:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves_list: list) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
