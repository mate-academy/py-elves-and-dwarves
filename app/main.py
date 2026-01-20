from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(all_players: list[Player]) -> int:
    return sum(player.get_rating() for player in all_players)


def elves_concert(all_elves: list[Elf]) -> None:
    for elf in all_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(all_dwarves: list[Dwarf]) -> None:
    for dwarf in all_dwarves:
        dwarf.eat_favourite_dish()
