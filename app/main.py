from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team_players: list[Player]) -> int:
    return sum(each.get_rating() for each in team_players)


def elves_concert(team_elves: list[Elf]) -> None:
    for player in team_elves:
        player.play_elf_song()


def feast_of_the_dwarves(team_dwarves: list[Dwarf]) -> None:
    for player in team_dwarves:
        player.eat_favourite_dish()
