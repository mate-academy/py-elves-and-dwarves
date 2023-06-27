from app.players.player import Player
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players: list[Player]) -> int:
    team_total_rating = 0
    for player in players:
        team_total_rating += player.get_rating()
    return team_total_rating


def elves_concert(elfs: list[Druid, ElfRanger]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(
        dwarfs: list[DwarfWarrior, DwarfBlacksmith]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
