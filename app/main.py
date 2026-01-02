from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)

def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()
        
def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()