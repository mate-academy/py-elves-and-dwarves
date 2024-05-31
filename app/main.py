from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf

def calculate_team_total_rating(team: list) -> int:
    result = 0
    for player in team:
        result += player.get_rating()
    return result

def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwar in dwarves:
        dwar.eat_favourite_dish()
