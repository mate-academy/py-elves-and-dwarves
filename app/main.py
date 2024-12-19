from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    result = 0
    for player in players:
        result += player.get_rating()
    return result


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()



