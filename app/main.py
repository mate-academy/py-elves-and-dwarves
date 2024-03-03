from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: Player) -> int:
    return sum([member.get_rating() for member in team])


def elves_concert(elves: Elf) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: Dwarf) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
