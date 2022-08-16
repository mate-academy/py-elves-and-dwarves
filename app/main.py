from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team):
    sum = 0
    for player in team:
        sum += player.get_rating()
        return sum


def elves_concert(list):
    for elfs in list:
        Elf.play_elf_song(elfs)


def feast_of_the_dwarves(list):
    for dwarfs in list:
        Dwarf.eat_favourite_dish(dwarfs)
