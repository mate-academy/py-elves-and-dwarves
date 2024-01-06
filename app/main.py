<<<<<<< HEAD
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elves: list[Elf]) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarfs: list[Dwarf]) -> None:
    for dwarf in list_of_dwarfs:
=======
def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elfs: list) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
>>>>>>> 568e491d132a50ab431b8ac70022f516afe278f8
        dwarf.eat_favourite_dish()
