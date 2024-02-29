from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.Player import Player


def calculate_team_total_rating(team: list[Player]) -> None:
    total = 0
    for player in team:
        total += player.get_rating()

    return total


def elves_concert(elf_list: list[Elf]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
