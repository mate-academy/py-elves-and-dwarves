from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player_list: list[Player]) -> int:
    all_rating = 0
    for i in player_list:
        all_rating += i.get_rating()
    return all_rating


def elves_concert(elf_list: list[Elf]) -> None:
    for i in elf_list:
        i.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for i in dwarf_list:
        i.eat_favourite_dish()
