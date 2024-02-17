from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list) -> int:
    total = 0
    for player in team:
        if isinstance(player, Player):
            total += player.get_rating()
    return total


def elves_concert(elves: list) -> None:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
