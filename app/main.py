from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(player_list: list[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elves_list: list[Elf]) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
