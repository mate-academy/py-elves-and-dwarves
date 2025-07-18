from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: ["Player"]) -> int:
    total = 0
    if team:
        for member in team:
            result = member.get_rating()
            total += result
        return total
    else:
        return 0


def elves_concert(elves: ["Elf"]) -> None:
    for member in elves:
        member.play_elf_song()


def feast_of_the_dwarves(dwarves: ["Dwarf"]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
