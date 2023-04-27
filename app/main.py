from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    """Calculate the total rating of a team."""
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    """Play an elf song for each elf in the given list."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """Have each dwarf in the given list eat their favourite dish."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
