from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    count_of_power = 0
    for player in players:
        if isinstance(player, ElfRanger):
            count_of_power += player.get_rating()

        if isinstance(player, DwarfWarrior):
            count_of_power += player.get_rating()

        if isinstance(player, Druid):
            count_of_power += player.get_rating()

        if isinstance(player, DwarfBlacksmith):
            count_of_power += player.get_rating()
    return count_of_power


def elves_concert(elves_list: list[Elf]) -> None:
    for elves in elves_list:
        elves.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarves in dwarf_list:
        dwarves.eat_favourite_dish()
