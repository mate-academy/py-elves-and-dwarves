from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(gamers: list[Player]) -> int:
    sum_rating = 0
    for rate in gamers:
        sum_rating += rate.get_rating()
    return sum_rating


def elves_concert(songs: list[Elf]) -> None:
    for song in songs:
        song.play_elf_song()


def feast_of_the_dwarves(dishes: list[Dwarf]) -> None:
    for dish in dishes:
        dish.eat_favourite_dish()
