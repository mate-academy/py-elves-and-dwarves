from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    rating_sum = 0
    for player in players:
        rating_sum += player.get_rating()
    return rating_sum


def elves_concert(elfs: list[[Elf]]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[[Dwarf]]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
