from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list[Elf]) -> None:
    [elv.play_elf_song() for elv in elves]


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarfs]
