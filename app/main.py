from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(member.get_rating() for member in team)


def elves_concert(elfs_team: list[Elf]) -> None:
    for elf_member in elfs_team:
        elf_member.play_elf_song()


def feast_of_the_dwarves(dwarfs_team: list[Dwarf]) -> None:
    for dwarf_member in dwarfs_team:
        dwarf_member.eat_favourite_dish()
