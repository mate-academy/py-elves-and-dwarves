from app.players.dwarves.dwarf_warrior import Dwarf
from app.players.elves.druid import Elf
from app.players.player import Player


def calculate_team_total_rating(members: list[Player]) -> int:
    return sum(member.get_rating() for member in members)


def elves_concert(members: list[Elf]) -> None:
    for elf in members:
        elf.play_elf_song()


def feast_of_the_dwarves(members: list[Dwarf]) -> None:
    for member in members:
        member.eat_favourite_dish()
