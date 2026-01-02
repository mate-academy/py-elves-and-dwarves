from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf

def calculate_team_total_rating(players: list) -> int:
    rating = [player.get_rating() for player in players]
    return sum(rating)

def elves_concert( players : list) -> str:
    for player in players:
        if isinstance(player, Elf):
            player.play_elf_song()
        
def feast_of_the_dwarves(players: list) -> str:
    for player in players:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()