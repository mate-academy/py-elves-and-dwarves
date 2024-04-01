from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player_list: list[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(list_elfs: list[Elf]) -> None:
    [elf.play_elf_song() for elf in list_elfs]


def feast_of_the_dwarves(dw_list: list[Dwarf]) -> None:
    [dw.eat_favourite_dish() for dw in dw_list]
