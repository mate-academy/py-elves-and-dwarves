from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(player.get_rating() for player in players_list)


def elves_concert(elves_list: list[Elf]) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_list: list[Dwarf]) -> None:
    for dwarf in dwarfs_list:
        dwarf.eat_favourite_dish()
