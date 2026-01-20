from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players_list: [Player]) -> int:
    total_rating = 0
    for player in players_list:
        if isinstance(player, Player):
            total_rating += player.get_rating()
    return total_rating


def elves_concert(elf_list: [Elf]) -> None:
    for elf in elf_list:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: [Dwarf]) -> None:
    for dwarf in dwarf_list:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
