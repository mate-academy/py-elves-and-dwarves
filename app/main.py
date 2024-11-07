from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    rating = 0
    for player in players:
        if isinstance(player, Player):
            rating += player.get_rating()

    return rating


def elves_concert(elves: list) -> None:
    for elv in elves:
        if isinstance(elv, Elf):
            elv.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
