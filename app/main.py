from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    sum = 0
    for player in players:
        sum += player.get_rating()
    return sum


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarws: list[Dwarf]) -> None:
    for dwarw in dwarws:
        dwarw.eat_favourite_dish()
