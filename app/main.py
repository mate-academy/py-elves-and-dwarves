from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(teams: list[Player]) -> int:
    return sum(player.get_rating() for player in teams)


def elves_concert(songs: list[Elf]) -> None:
    for song in songs:
        song.play_elf_song()


def feast_of_the_dwarves(eats: list[Dwarf]) -> None:
    for eat in eats:
        eat.eat_favourite_dish()
