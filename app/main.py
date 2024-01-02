from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(each_player.get_rating() for each_player in players)


def elves_concert(elves: list[Elf]) -> None:
    for each_elf in elves:
        each_elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for each_dwarf in dwarves:
        each_dwarf.eat_favourite_dish()
