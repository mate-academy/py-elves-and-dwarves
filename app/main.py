from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: Player) -> int:
    return sum([char.get_rating() for char in players_list])


def elves_concert(elves_list: list[Elf]) -> None:
    [elf.play_elf_song() for elf in elves_list]


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves_list]
