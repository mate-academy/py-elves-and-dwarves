from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = [player.get_rating() for player in players]
    return sum(total_rating)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
