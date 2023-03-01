from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(play.get_rating() for play in players_list)


def elves_concert(list_elf: list[Elf]) -> None:
    for elf in list_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarw: list[Dwarf]) -> None:
    for dwar in list_dwarw:
        dwar.eat_favourite_dish()
