from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:

    return sum(hero.get_rating() for hero in team)


def elves_concert(team: list[Elf]) -> None:
    [hero.play_elf_song() for hero in team]


def feast_of_the_dwarves(team: list[Dwarf]) -> None:
    [hero.eat_favourite_dish() for hero in team]
