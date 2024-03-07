from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_group: list[Player]) -> int:
    return sum(player.get_rating() for player in players_group)


def elves_concert(elves_group: list[Elf]) -> None:
    for elf in elves_group:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_group: list[Dwarf]) -> None:
    for dwarf in dwarves_group:
        dwarf.eat_favourite_dish()
