from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(
        gamers: list[Player]
) -> int:
    """
    Calculate the sum of the ranting of a party.

    Args:
        gamers (list[Player]): Players' avatars.

    Returns:
        int: sum of the players' rating.
    """
    total_rating = 0
    for gamer in gamers:
        total_rating += gamer.get_rating()

    return total_rating


def elves_concert(
        elves: list[Elf]
) -> None:
    """
    Let the elf players play at a concert.

    Args:
        elves (list[Elf]): Players of the elven race.
    """
    for elf_player in elves:
        elf_player.play_elf_song()


def feast_of_the_dwarves(
        dwarves: list[Dwarf]
) -> None:
    """
    Let the dwarf players have a fest.

    Args:
        dwarves (list[Dwarf]): player of the dwarven race.
    """
    for dwarf_player in dwarves:
        dwarf_player.eat_favourite_dish()
