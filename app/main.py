
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> str:
    for elf in elves:
        concert = elf.play_elf_song()
    return concert


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> str:
    for dwarf in dwarves:
        feast = dwarf.eat_favourite_dish()
    return feast
