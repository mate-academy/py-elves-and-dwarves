from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves_team: list[Elf]) -> None:
    for elf in elves_team:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_team: list[Dwarf]) -> None:
    for obj in dwarfs_team:
        obj.eat_favourite_dish()
