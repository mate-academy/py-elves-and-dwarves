from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    rating_count = 0
    for player in players:
        rating_count += player.get_rating()
    return rating_count


def elves_concert(elf_players: list[Elf]) -> None:
    for elf in elf_players:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_players: list[Dwarf]) -> None:
    for dwarf in dwarf_players:
        dwarf.eat_favourite_dish()
