from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(musicians: list[Elf]) -> None:
    for musician in musicians:
        musician.play_elf_song()


def feast_of_the_dwarves(guests: list[Dwarf]) -> None:
    for guest in guests:
        guest.eat_favourite_dish()
