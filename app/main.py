from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list) -> None:
    for elf in elves:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        Dwarf.eat_favourite_dish(dwarf)
