from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    total_rating = sum(player.get_rating() for player in team)
    return total_rating


def elves_concert(elvse: [Elf]) -> None:
    for elf in elvse:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: [Dwarf]) -> None:
    for dwarv in dwarves:
        dwarv.eat_favourite_dish()
