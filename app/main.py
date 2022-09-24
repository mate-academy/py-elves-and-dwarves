from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players_ls: list[Player]) -> int:

    return sum(player.get_rating() for player in players_ls)


def elves_concert(elf_ls: list[Elf]) -> None:

    for elf in elf_ls:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_ls: list[Dwarf]) -> None:

    for dwarf in dwarf_ls:
        dwarf.eat_favourite_dish()
