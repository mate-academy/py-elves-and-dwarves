from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elves: list[Elf]) -> None:
    for elv in list_of_elves:
        if isinstance(elv, Elf):
            elv.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
