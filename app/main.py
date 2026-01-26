from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.rating for player in players)


def elves_concert(elves: list[Elf]) -> int:
    return sum(elf.rating + elf.magic_power for elf in elves)


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> int:
    return sum(dwarf.rating + dwarf.strength for dwarf in dwarves)
