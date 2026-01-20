from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(player_rating_list: list[Player]) -> int:
    result = 0
    for rate in player_rating_list:
        result += rate.get_rating()

    return result


def elves_concert(concert: list[Elf]) -> None:
    for elfs in concert:
        elfs.play_elf_song()


def feast_of_the_dwarves(fest: list[Dwarf]) -> None:
    for dwarfs in fest:
        dwarfs.eat_favourite_dish()
