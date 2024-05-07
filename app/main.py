from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: Player) -> int:
    total_rating = 0
    total_rating = sum(player.get_rating() for player in players)
    return total_rating


def elves_concert(singers: Elf) -> str:
    for singer in singers:
        singer.play_elf_song()


def feast_of_the_dwarves(eaters: Dwarf) -> str:
    for eater in eaters:
        eater.eat_favourite_dish()
