from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    return sum(user.get_rating() for user in team)


def elves_concert(elves: list) -> list:
    result1 = []
    for user_elf in elves:
        result1.append(Elf.play_elf_song(user_elf))
    return result1


def feast_of_the_dwarves(dwarves: list) -> list:
    result = []
    for user_dwarf in dwarves:
        result.append(Dwarf.eat_favourite_dish(user_dwarf))
    return result
