from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Elf | Dwarf]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf_list: list[Elf]) -> None:
    for elf in elf_list:
        if isinstance(elf, (Druid, ElfRanger)):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list[Dwarf]) -> None:
    for dwarf in dwarves_list:
        if isinstance(dwarf, (DwarfWarrior, DwarfBlacksmith)):
            dwarf.eat_favourite_dish()
