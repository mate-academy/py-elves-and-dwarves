from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(team_elf: list[Elf]) -> None:
    for one_elf in team_elf:
        one_elf.play_elf_song()


def feast_of_the_dwarves(team_dwarf: list[Dwarf]) -> None:
    for one_dwarf in team_dwarf:
        one_dwarf.eat_favourite_dish()
