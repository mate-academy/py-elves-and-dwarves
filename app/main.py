from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players: list) -> int:

    return sum(player.get_rating() for player in players)

def elves_concert(elfs: list) -> None:

    for elf in elfs:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarfs: list) -> None:

    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
