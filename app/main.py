from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: dict[Player]) -> int:
    total_rate = 0
    for hero in players:
        total_rate += hero.get_rating()
    return total_rate


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
