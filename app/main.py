from app.players.player import Player
from app.players.dwarves.dwart import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_reting(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
