from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list):
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list):
    for elf in elves:
        if issubclass(elf.__class__, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        if issubclass(dwarf.__class__, Dwarf):
            dwarf.eat_favourite_dish()
