from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(the_team: list[Player]) -> int:
    res = 0

    for player in the_team:
        res += player.get_rating()

    return res

def elves_concert(the_elves: list[Elf]) -> None:
    for elf in the_elves:
        elf.play_elf_song()

def feast_of_the_dwarves(the_dwarves: list[Dwarf]) -> None:
    for dwarf in the_dwarves:
        dwarf.eat_favourite_dish()
