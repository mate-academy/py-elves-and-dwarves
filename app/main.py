from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(names: list[Player]) -> int:
    return sum(i.get_rating() for i in names)

def elves_concert(names: list[Elf]) -> None:
    for i in names :
        i.play_elf_song()

def feast_of_the_dwarves(names: list[Dwarf]) -> None:
    for i in names :
        i.eat_favourite_dish()
