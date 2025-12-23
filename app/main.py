from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for singer in elves:
        singer.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarw in dwarves:
        dwarw.eat_favourite_dish()
