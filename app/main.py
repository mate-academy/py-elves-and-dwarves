from app.players.dwarves import Dwarf
from app.players.elves import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    """Calculates total power rating for all players in list"""
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    """Calls .play_elf_song() for each Elf in list"""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """Calls .eat_favourite_dish() for each Dwarf in list"""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
