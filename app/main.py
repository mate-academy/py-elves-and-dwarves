from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> None:
    return sum(player.get_rating() for player in players)


def elves_concert(list_elf: list[Elf]) -> None:
    for elf in list_elf:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(list_dwarf: list[Dwarf]) -> None:
    for dwarf in list_dwarf:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
