from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: [Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves_dict: [Elf]) -> None:
    for elf in elves_dict:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_dict: [Dwarf]) -> None:
    for dwarf in dwarves_dict:
        dwarf.eat_favourite_dish()
