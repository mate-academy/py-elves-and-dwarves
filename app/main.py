from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        print(f"{elf.nickname} is playing a song on the "
              f"{elf.musical_instrument}")


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
