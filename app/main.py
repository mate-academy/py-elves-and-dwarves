from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elf_players: list[Elf]) -> None:
    for elf in elf_players:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_players: list[Dwarf]) -> None:
    for dwarf in dwarf_players:
        dwarf.eat_favourite_dish()
