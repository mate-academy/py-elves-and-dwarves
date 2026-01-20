from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team):
    count_point_of_team = 0
    for heroy_of_team in team:
        count_point_of_team += heroy_of_team.get_rating()
    return count_point_of_team


def elves_concert(heroes: list[Elf]):
    for heroy in heroes:
        heroy.play_elf_song()


def feast_of_the_dwarves(heroes: list[Dwarf]):
    for heroy in heroes:
        heroy.eat_favourite_dish()
