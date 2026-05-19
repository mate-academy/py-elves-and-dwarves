from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team_players: list[Player]) -> int:
    return sum(player_rating.get_rating() for player_rating in team_players)


def elves_concert(elf_list: list[Elf]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list[Dwarf]) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()
