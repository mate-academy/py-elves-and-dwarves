from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: [Player]) -> int:
    result = 0
    for player in players:
        result += player.get_rating()
    return result


def elves_concert(elfs: [Elf]) -> None:
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: [Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
