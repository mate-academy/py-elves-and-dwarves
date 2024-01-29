from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list[Elf | Druid | ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf
                                       | DwarfBlacksmith
                                       | DwarfWarrior]) -> None:
    for drawf in dwarves:
        drawf.eat_favourite_dish()
