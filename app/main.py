from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(player_list: list[Player]) -> int:
    return sum(player.get_rating() for player in player_list)


def elves_concert(elf_list: list[Elf]) -> None:
    for song in elf_list:
        song.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dish in dwarf_list:
        dish.eat_favourite_dish()
