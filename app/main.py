from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players: list[Player]) -> int:
    rating = 0
    for player in players:
        if isinstance(player, DwarfWarrior):
            rating += DwarfWarrior.get_rating(player)
        if isinstance(player, DwarfBlacksmith):
            rating += DwarfBlacksmith.get_rating(player)
        if isinstance(player, Druid):
            rating += Druid.get_rating(player)
        if isinstance(player, ElfRanger):
            rating += ElfRanger.get_rating(player)
    return rating


def elves_concert(elfs: list[Elf]) -> None:
    for elf in elfs:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        Dwarf.eat_favourite_dish(dwarf)
