from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elfes: list[Elf]) -> str:
    for elf in elfes:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfes: list[Dwarf]) -> str:
    for dwarf in dwarfes:
        dwarf.eat_favourite_dish()
