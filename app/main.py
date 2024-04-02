from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player_list: list[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(list_elfs: list[Elf]) -> None:
    for elf in list_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
