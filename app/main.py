from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(song: list[Elf]) -> None:
    for sound in song:
        sound.play_elf_song()


def feast_of_the_dwarves(dish: list[Dwarf]) -> None:
    for eat in dish:
        eat.eat_favourite_dish()
