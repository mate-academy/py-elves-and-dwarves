from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior  # noqa: F401
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith  # noqa: F401
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger  # noqa: F401
from app.players.elves.druid import Druid  # noqa: F401


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
