from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_player: list[Player]) -> int:
    rating_player = 0
    for player in list_of_player:
        rating = player.get_rating()
        rating_player += rating
    return rating_player


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
