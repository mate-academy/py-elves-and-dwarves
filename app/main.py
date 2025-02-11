from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = 0
    for pl in players:
        total_rating += pl.get_rating()
    return total_rating


def elves_concert(elves: list[Elf]) -> str:
    return "\n".join(e.play_elf_song() for e in elves)


def feast_of_the_dwarves(dwarf: list[Dwarf]) -> str:
    return "\n".join(d.eat_favourite_dish() for d in dwarf)
