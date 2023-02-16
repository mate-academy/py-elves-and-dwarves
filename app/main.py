from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(member.get_rating() for member in team)


def elves_concert(elves: list[Elf]) -> list[None]:
    return [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> list[None]:
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
