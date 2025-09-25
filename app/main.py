import pytest
import io
from contextlib import redirect_stdout

from app.main import calculate_team_total_rating, elves_concert, feast_of_the_dwarves
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith

def calculate_team_total_rating(players: list[Player]) -> int:
    """Zwraca sumę ratingów wszystkich graczy w zespole."""
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    """Wywołuje metodę play_elf_song dla wszystkich elfów w liście."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """Wywołuje metodę eat_favourite_dish dla wszystkich krasnoludów w liście."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
