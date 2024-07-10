from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list) -> int:
    return sum(teammate.get_rating() for teammate in team
               if isinstance(teammate, Player))


def elves_concert(elves: list) -> None:
    [elf.play_elf_song() for elf in elves
     if isinstance(elf, Elf)]


def feast_of_the_dwarves(dwarves: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves
     if isinstance(dwarf, Dwarf)]
