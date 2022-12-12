from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    if not team:
        return 0
    summa = 0
    for player in team:
        summa += player.get_rating()
    return summa


def elves_concert(elves: list[Elf]) -> None:
    for single in elves:
        single.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
