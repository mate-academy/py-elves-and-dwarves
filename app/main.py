from app.players.dwarves import dwarf
from app.players.elves import elf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[elf]) -> None:
    for elv in elves:
        elv.play_elf_song()


def feast_of_the_dwarves(dwarves: list[dwarf]) -> None:
    for dwarf_ in dwarves:
        dwarf_.eat_favourite_dish()
