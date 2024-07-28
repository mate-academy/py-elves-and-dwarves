from app.players.player import Player

from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_players: [Player]) -> int:
    return sum(player.get_rating() for player in list_players)


def elves_concert(list_elves: [Elf]) -> None:
    for elf in list_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarves: [Dwarf]) -> None:
    for dwarf in list_dwarves:
        dwarf.eat_favourite_dish()
