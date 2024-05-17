from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> float:
    return sum(players.get_rating() for players in players)


def elves_concert(players: list[Elf]) -> None:
    for elf in players:
        elf.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for dwarf in players:
        dwarf.eat_favourite_dish()
