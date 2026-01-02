from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf

#this is my main function

def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)

def elves_concert( players : list) -> None:
    for player in players:
        if isinstance(player, Elf):
            player.play_elf_song()
        
def feast_of_the_dwarves(players: list) -> None:
    for player in players:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()