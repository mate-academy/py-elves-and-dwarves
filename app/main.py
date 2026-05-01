from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    res = 0
    for player in players:
        res += player.get_rating()
    return res


def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
