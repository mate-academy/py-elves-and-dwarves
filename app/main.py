from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    result = 0
    for member in team:
        result += member.get_rating()

    return result

def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dworf in dwarves:
        dworf.eat_favourite_dish()
