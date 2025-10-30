from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int | float:
    return sum(player.get_rating() for player in players)


def elves_concert(players: list) -> None:
    for player in players:
        if isinstance(player, Elf):
            player.play_elf_song()


def feast_of_the_dwarves(players: list) -> None:
    for player in players:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()
