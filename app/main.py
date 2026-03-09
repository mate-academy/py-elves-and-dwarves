from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(member.get_rating() for member in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        if not isinstance(elf, Elf):
            raise TypeError("The player must be an Elf to play songs")
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        if not isinstance(dwarf, Dwarf):
            raise TypeError("The player must be a Dwarf to partake in a feast")
        dwarf.eat_favourite_dish()
