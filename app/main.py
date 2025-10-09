from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    total = 0
    for player in players_list:
        total += player.get_rating()
    return total


def elves_concert(elf_list: list[Elf]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
