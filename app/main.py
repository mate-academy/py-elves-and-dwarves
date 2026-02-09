from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player: Player) -> int:
    return sum(rating.get_rating() for rating in player)


def elves_concert(elf: Elf) -> None:
    for item in elf:
        item.play_elf_song()


def feast_of_the_dwarves(dwarf: Dwarf) -> None:
    for item in dwarf:
        item.eat_favourite_dish()
