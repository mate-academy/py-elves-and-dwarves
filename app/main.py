from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: ["Player"]) -> int:
    if team:
        for player in team:
            return sum([player.get_rating() for player in team])
    else:
        return 0


def elves_concert(elves: ["Elf"]) -> None:
    for elves in elves:
        elves.play_elf_song()


def feast_of_the_dwarves(dwarves: ["Dwarf"]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
