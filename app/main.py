from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player_member.get_rating() for player_member in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf_member in elves:
        elf_member.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf_member in dwarfs:
        dwarf_member.eat_favourite_dish()
