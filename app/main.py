from app.players.player import Player
from app.players.elves.elf import Elf
# from app.players.elves.druid import Druid
# from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elfs: list[Elf]) -> None:
    [elf.play_elf_song() for elf in elfs]


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarfs]
