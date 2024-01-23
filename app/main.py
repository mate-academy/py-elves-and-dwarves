from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = 0

    for player in players:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(elvs: list[Elf]) -> None:
    for elv in elvs:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
