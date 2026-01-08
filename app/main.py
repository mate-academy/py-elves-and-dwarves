from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    """Return the sum of all player ratings in the team."""
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    """Make each elf play their song."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """Make each dwarf eat their favourite dish."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
