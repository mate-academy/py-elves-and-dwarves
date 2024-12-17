from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(list_of_elf: list[Elf]) -> None:
    [elf.play_elf_song() for elf in list_of_elf]


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in list_of_dwarves]
