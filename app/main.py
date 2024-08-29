from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid


def calculate_team_total_rating(team: list[Player]) -> int:
    spell = 0
    rating = 0
    for player in team:
        if isinstance(player, Druid):
            spell += player.get_rating()
        else:
            rating += player.get_rating()
    return spell + rating


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
