from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(ls: list[Player]) -> int:
    return sum(player.get_rating() for player in ls)


def elves_concert(ls: list[Elf]) -> None:
    for elf in ls:
        elf.play_elf_song()


def feast_of_the_dwarves(ls: list[Dwarf]) -> None:
    for dwarf in ls:
        dwarf.eat_favourite_dish()
