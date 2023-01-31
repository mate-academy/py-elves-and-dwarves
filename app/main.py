from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger


elves_list = []
dwarves_list = []


def calculate_team_total_rating(players: list) -> int:
    total_rating = 0
    for player in players:
        if isinstance(player, DwarfBlacksmith):
            dwarves_list.append(player)
            total_rating += DwarfBlacksmith.get_rating(player)
        if isinstance(player, DwarfWarrior):
            dwarves_list.append(player)
            total_rating += DwarfWarrior.get_rating(player)
        if isinstance(player, Druid):
            elves_list.append(player)
            total_rating += Druid.get_rating(player)
        if isinstance(player, ElfRanger):
            elves_list.append(player)
            total_rating += ElfRanger.get_rating(player)
    return total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        Dwarf.eat_favourite_dish(dwarf)
