from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    rating = 0
    for player in players:
        rating += player.get_rating()
    return rating


def elves_concert(elf_song: list[Elf]) -> None:
    for elf in elf_song:
        elf.play_elf_song()


def feast_of_the_dwarves(favourite_dish: list[Dwarf]) -> None:
    for dwarf_dish in favourite_dish:
        dwarf_dish.eat_favourite_dish()
