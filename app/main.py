from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player
from app.players.elves.elf import Elf


def calculate_team_total_rating(list_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_players)


def elves_concert(list_elfs: list[Elf]) -> None:
    for elf in list_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_dwarves: list[Dwarf]) -> None:
    for dwarve in list_dwarves:
        dwarve.eat_favourite_dish()
