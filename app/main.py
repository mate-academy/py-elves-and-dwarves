from app.players import player
from app.players.elves import elf
from app.players.dwarves import dwarf


def calculate_team_total_rating(players: list[player.Player]) -> int:
    return sum(each_player.get_rating() for each_player in players)


def elves_concert(elves: list[elf.Elf]) -> None:
    for each_elf in elves:
        each_elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[dwarf.Dwarf]) -> None:
    for each_dwarf in dwarves:
        each_dwarf.eat_favourite_dish()
