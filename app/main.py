from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    all_rating = [i.get_rating() for i in team]
    return sum(all_rating)


def elves_concert(elves: list[Elf]) -> None:
    for i in elves:
        i.play_elf_song()


def feast_of_the_dwarves(dwarwes: list[Dwarf]) -> None:
    for i in dwarwes:
        i.eat_favourite_dish()
