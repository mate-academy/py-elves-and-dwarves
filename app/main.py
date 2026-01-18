from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(listt: [Player]) -> int | float:
    total = 0
    for ls in listt:
        total += ls.get_rating()
    return total


def elves_concert(listt: [Elf]) -> None:
    for ls in listt:
        ls.play_elf_song()


def feast_of_the_dwarves(listt: [Dwarf]) -> None:
    for ls in listt:
        ls.eat_favourite_dish()
