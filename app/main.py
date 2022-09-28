from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(players: list) -> int:
    team_list = [(player.get_rating()) for player in players]
    print(sum(team_list))
    return sum(team_list)


def elves_concert(elves: list):
    for elf in elves:
        Elf.play_elf_song(elf)


def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        Dwarf.eat_favourite_dish(dwarf)
