from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def calculate_team_total_rating(team: list) -> None:
    total = 0
    for player in team:
        one_player = player.get_rating()
        total += one_player
    return total


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
