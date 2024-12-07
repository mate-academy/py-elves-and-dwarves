from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves_band: list[Elf]) -> None:
    for elf_musician in elves_band:
        elf_musician.play_elf_song()


def feast_of_the_dwarves(eating_dwarves: list[Dwarf]) -> None:
    for dwarf_eater in eating_dwarves:
        dwarf_eater.eat_favourite_dish()
