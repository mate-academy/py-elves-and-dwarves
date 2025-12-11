from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list):
    """
    Takes a list of Players and returns the sum of the ratings
    for all team members.
    """
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]):
    """
    Takes a list of Elf instances and calls play_elf_song
    method for each elf.
    """
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]):
    """
    Takes a list of Dwarf instances and calls eat_favourite_dish
    method for each dwarf.
    """
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
