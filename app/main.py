from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(team_member.get_rating() for team_member in team)


def elves_concert(band: list[Elf]) -> None:
    for musician in band:
        musician.play_elf_song()


def feast_of_the_dwarves(party: list[Dwarf]) -> None:
    for dwarf in party:
        dwarf.eat_favourite_dish()
