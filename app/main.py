from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(team: Player) -> int:
    result = 0
    for member in team:
        result += member.get_rating()
    return result


def elves_concert(arr: Elf) -> str:
    for i in arr :
        i.play_elf_song()


def feast_of_the_dwarves(arr: Dwarf) -> str:
    for i in arr:
        i.eat_favourite_dish()
