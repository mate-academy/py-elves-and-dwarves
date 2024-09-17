from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(gamers: list[Player]) -> int:
    return sum([gamer.get_rating() for gamer in gamers])


def elves_concert(elfs: list[Elf]) -> None:
    for elfes in elfs:
        elfes.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
