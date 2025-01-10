from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list) -> int:

    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(players: list | Elf) -> None:
    for player in players:
        Elf.play_elf_song(player)


def feast_of_the_dwarves(players: list | Dwarf) -> None:
    for player in players:
        Dwarf.eat_favourite_dish(player)
