from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(player: list) -> int:
    return sum(player.get_rating()
               for player in player)


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf in dwarf_list:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
