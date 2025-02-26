from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


def elves_concert(musicians: list[Elf]) -> None:
    for musician in musicians:
        musician.play_elf_song()


def calculate_team_total_rating(players: list[Player]) -> int | float:
    return sum(player.get_rating() for player in players)
