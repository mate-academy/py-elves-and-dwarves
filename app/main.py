from app.players.player import Player

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(musicians: list[Elf]) -> None:
    for musician in musicians:
        musician.play_elf_song()


def feast_of_the_dwarves(list_of_feasters: list[Dwarf]) -> None:
    for gimli in list_of_feasters:
        gimli.eat_favourite_dish()
