from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int | float:
    """
    Returns the sum of the ratings for all team members.
    :param team: Player
    :return: int | float
    """
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    """
    Calls 'play_elf_song' method for each Elf.
    :param elves: Elf
    :return: None
    """
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """
    Calls 'eat_favourite_dish' method for each Dwarf.
    :param dwarves: Dwarf
    :return: None
    """
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
