from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(elves_team: [Player]) -> int:
    return sum(member.get_rating() for member in elves_team)


def elves_concert(elves_team: [Elf]) -> None:
    for elf in elves_team:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_team: [Dwarf]) -> None:
    for dwarf in dwarves_team:
        dwarf.eat_favourite_dish()
