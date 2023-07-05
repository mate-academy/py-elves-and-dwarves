from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    sum_of_rating = 0

    for player in players:
        sum_of_rating += player.get_rating()

    return sum_of_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        if issubclass(elf.__class__, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        if issubclass(dwarf.__class__, Dwarf):
            dwarf.eat_favourite_dish()
