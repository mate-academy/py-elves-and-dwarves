from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    sum_of_ratings = sum(player.get_rating() for player in players)
    return sum_of_ratings

def elves_concert(elves: list[Elf]) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarfes: list[Dwarf]) -> None:
    for dwarf in dwarfes:
        dwarf.eat_favourite_dish()
