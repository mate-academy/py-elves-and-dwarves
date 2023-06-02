from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: list[Player]) -> int:
    count = 0
    for i in players_list:
        count += i.get_rating()
    return count


def elves_concert(players_list: list[Elf]) -> None:
    for i in players_list:
        i.play_elf_song()


def feast_of_the_dwarves(players_list: list[Dwarf]) -> None:
    for i in players_list:
        i.eat_favourite_dish()
