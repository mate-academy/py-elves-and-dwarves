from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:

    return sum(person.get_rating() for person in team)


def elves_concert(elves: list[Elf]) -> None:

    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarver: list[Dwarf]) -> None:

    [dwarf.eat_favourite_dish() for dwarf in dwarver]
