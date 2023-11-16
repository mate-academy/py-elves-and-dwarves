from app.players.player import Player

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_players: list[Player]) -> int:
    result_score = 0
    for player in list_players:
        result_score += player.get_rating()
    return result_score


def elves_concert(list_elfs: list[Elf]) -> None:
    for elf in list_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list[Dwarf]) -> None:
    for dwarf in list_dwarves:
        dwarf.eat_favourite_dish()
