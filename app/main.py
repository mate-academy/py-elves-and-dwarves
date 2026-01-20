from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(group: list[Elf]) -> None:
    [member.play_elf_song() for member in group]


def feast_of_the_dwarves(group: list[Dwarf]) -> None:
    [member.eat_favourite_dish() for member in group]
