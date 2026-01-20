from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elfs: list[Elf]) -> list:
    [elf.play_elf_song() for elf in elfs]


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> list:
    [dwarf.eat_favourite_dish() for dwarf in dwarves]
