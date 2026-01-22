from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    res = sum(player.get_rating() for player in players)
    return 0 if res is None else res


def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()
