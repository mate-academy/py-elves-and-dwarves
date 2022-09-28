from app.players.elves import elf
from app.players.dwarves import dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[elf]) -> None:
    for elfs in elves:
        elfs.play_elf_song()


def feast_of_the_dwarves(dwarves: list[dwarf]) -> None:
    for dwarfs in dwarves:
        dwarfs.eat_favourite_dish()
