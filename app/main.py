from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf

from app.players.elves.elf import Elf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs: list[Dwarf]) -> None:
    for dwarf in list_of_dwarfs:
        dwarf.eat_favourite_dish()
