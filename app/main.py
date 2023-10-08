from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_players: list["Player"]) -> int:
    total_rating = 0
    for player in list_players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(list_elves: list["Elf"]) -> None:
    for elves in list_elves:
        elves.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list["Dwarf"]) -> None:
    for dwarf in list_dwarves:
        dwarf.eat_favourite_dish()
