from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> float:
    return sum([player.get_rating() for player in team])


def elves_concert(team: list[Elf]) -> None:
    for player in team:
        player.play_elf_song()


def feast_of_the_dwarves(dw: list[Dwarf]) -> None:
    for dwarf in dw:
        print(f"{dwarf.nickname} is eating {dwarf._favourite_dish}")
