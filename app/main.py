from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    result = 0
    for item in players:
        result += item.get_rating()
    return result


def elves_concert(player: list[Elf]) -> None:
    for item2 in player:
        item2.play_elf_song()


def feast_of_the_dwarves(player: list[Dwarf]) -> None:
    for item3 in player:
        item3.eat_favourite_dish()
