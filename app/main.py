from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior

def calculate_team_total_rating(team: list) -> int:
    total_rating = 0
    for member in team:
        total_rating =+ member.get_rating()
    return total_rating

def elves_concert(team_elf: list) -> None:
    for member in team_elf:
        member.play_elf_song()

def feast_of_the_dwarves(team_dwarf: list) -> None:
    for member in team_dwarf:
        member.eat_favourite_dish()
