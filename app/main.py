from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(elfs_list: list[Elf]) -> None:
    [elf.play_elf_song() for elf in elfs_list]


def feast_of_the_dwarves(dwarfs_list: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarfs_list]
