from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player_list: list[Player]) -> int | float:
    return sum([player.get_rating() for player in player_list])


def elves_concert(elf_list: list[Elf]) -> None:
    [elf.play_elf_song() for elf in elf_list]


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarf_list]
