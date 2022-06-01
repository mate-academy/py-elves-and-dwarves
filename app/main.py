from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(total_rating: list):
    return sum(player.get_rating() for player in total_rating)


def elves_concert(elves: list):
    for music in elves:
        music.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for eat in dwarves:
        eat.eat_favourite_dish()
