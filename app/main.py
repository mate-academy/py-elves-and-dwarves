from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player_one.get_rating() for player_one in players)


def elves_concert(players: list[Elf]) -> None:
    for player_one in players:
        player_one.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf_one in dwarves:
        dwarf_one.eat_favourite_dish()
