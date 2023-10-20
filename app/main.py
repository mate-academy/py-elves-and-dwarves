from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: [Player]) -> int:
    sum_of_ratings = 0
    for player in players_list:
        sum_of_ratings += player.get_rating()

    return sum_of_ratings


def elves_concert(elves_list: [Elf]) -> None:
    for elf in elves_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: [Dwarf]) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
