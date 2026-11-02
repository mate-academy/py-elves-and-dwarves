from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(item.get_rating() for item in players_list)


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for item in list_of_elfs:
        item.play_elf_song()


def feast_of_the_dwarves(list_of_dwarf: list[Dwarf]) -> None:
    for item in list_of_dwarf:
        item.eat_favourite_dish()
