from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    """
    :param players: takes a list of Players
    :return: calculates the sum of the ratings for all team members
    """
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list[Elf]) -> None:
    """
    :param elves: takes a list of Elf and
    calls play_elf_song method for each elf
    """
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """
    :param dwarves: takes a list of Dwarf
    and calls eat_favourite_dish method for each dwarf.
    """
    [dwarf.eat_favourite_dish() for dwarf in dwarves]
