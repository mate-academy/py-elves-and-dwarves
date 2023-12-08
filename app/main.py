from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    total_rating = sum(player.get_rating() for player in team)
    return total_rating


def elves_concert(elves: list[Elf]) -> list[Elf]:
    return [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> list[Dwarf]:
    return[dwarf.eat_favourite_dish() for dwarf in dwarves]
