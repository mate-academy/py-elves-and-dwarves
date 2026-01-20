from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(ls_of_team: list[Player]) -> int:
    return sum(player.get_rating() for player in ls_of_team)


def elves_concert(ls_of_elves: list[Elf]) -> None:
    for elf in ls_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(ls_of_dwarfs: list[Dwarf]) -> None:
    for dwarf in ls_of_dwarfs:
        dwarf.eat_favourite_dish()
