from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(list_of_players: list) -> int:
    total_rating = 0
    for player in list_of_players:
        total_rating += player.get_rating()
    return total_rating

def elves_concert(list_of_elves: list) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()

def feast_of_the_dwarves(list_of_dwarves: list) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()
