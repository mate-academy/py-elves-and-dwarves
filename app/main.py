from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for elfs in list_of_elfs:
        elfs.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarfs in list_of_dwarves:
        dwarfs.eat_favourite_dish()
