from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    result = 0
    for gamers in players:
        result += gamers.get_rating()
    return result


def elves_concert(elves: list[Elf]) -> None:
    for elv in elves:
        Elf.play_elf_song(elv)


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwar in dwarves:
        Dwarf.eat_favourite_dish(dwar)
