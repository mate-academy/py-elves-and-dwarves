from players.player import Player
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf

def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)

def elves_concert(elves: list[Elf]):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: list[Dwarf]):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
