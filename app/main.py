from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(teams: list[Player]) -> int:
    return sum(player.get_rating() for player in teams)


def elves_concert(elves_: list[Elf]) -> None:
    for elf in elves_:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves_: list[Dwarf]) -> None:
    for dwarf in dwarves_:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()

