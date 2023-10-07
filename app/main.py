from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list) -> int:
    return sum(player_one.get_rating() for player_one in players)


def elves_concert(players: list) -> None:
    for player_one in players:
        if player_one is ElfRanger or player_one is Druid:
            player_one.play_elf_song


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf_one in dwarves:
        dwarf_one.eat_favorite_dish


# dwarves = [
#     DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
#     DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
# ]
# feast_of_the_dwarves(dwarves)
# # "Thiddeal is eating French Fries"
# # "Dwarf is eating Caesar Salad"









