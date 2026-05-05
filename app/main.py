from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    value = 0
    for player in players_list:
        value = value + player.get_rating()
    return value


def elves_concert(elves_list: list[Elf]) -> None :
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None :
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
