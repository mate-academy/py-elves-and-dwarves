from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(members: list[Player]) -> int:
    """
    Calculates the total rating of a team
    by summing up the ratings of all its members.
    """
    return sum(member.get_rating() for member in members)


def elves_concert(elf_members: list[Elf]) -> None:
    """
    Simulates an Elves concert, where each Elf plays an Elf song.
    """
    for elf in elf_members:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_members: list[Dwarf]) -> None:
    """
    Simulates a feast of the Dwarves,
    where each Dwarf eats their favourite dish.
    """
    for dwarf in dwarf_members:
        dwarf.eat_favourite_dish()
