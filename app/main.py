from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elf: list[Elf]) -> None:
    for elf in list_of_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarf: list[Dwarf]) -> None:
    for dwarf in list_of_dwarf:
        dwarf.eat_favourite_dish()
