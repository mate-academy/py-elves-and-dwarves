from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    total = 0
    for player in team:
        total += player.get_rating()
    return total


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
