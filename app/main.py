from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list):
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list):
    for elf in elves:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        Dwarf.eat_favourite_dish(dwarf)
