from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: dict[Player]) -> int:
    return sum(hero.get_rating() for hero in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
