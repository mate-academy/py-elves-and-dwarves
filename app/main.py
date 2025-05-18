from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(pl: [Player]) -> int:
    suma = 0
    for put in pl:
        suma += put.get_rating()
    return suma


def elves_concert(elfs: [Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: [Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
