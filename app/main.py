from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf
from app.players.player import Player


def calculate_team_total_rating(
        list_of_players: list[Player]
) -> int:
    if list_of_players:
        return sum(
            [player.get_rating() for player in list_of_players]
        )
    return 0


def elves_concert(list_of_elves: list[Elf]) -> None:
    [elf.play_elf_song() for elf in list_of_elves]


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    [dwarf.eat_favourite_dish() for dwarf in list_of_dwarves]
