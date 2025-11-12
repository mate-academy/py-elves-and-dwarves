from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    team_rating = 0
    for player in players:
        team_rating += player.get_rating()
    return team_rating


def elves_concert(elves: list[Elf]) -> str:
    for elve in elves:
        concert = elve.play_elf_song()
    return concert


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> str:
    for dwarf in dwarves:
        feast = dwarf.eat_favourite_dish()
    return feast
