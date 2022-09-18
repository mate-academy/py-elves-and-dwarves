from app.players.elves import elf
from app.players.dwarves import dwarf


def calculate_team_total_rating(team: list):
    if not team:
        return 0


def elves_concert(elves: list):
    return [elf.Elf.play_elf_song(elv) for elv in elves]


def feast_of_the_dwarves(dwarves: list):
    return [dwarf.Dwarf.eat_favourite_dish(dwar) for dwar in dwarves]
