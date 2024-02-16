from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team_list: list) -> int:
    return sum(player.get_rating() for player in team_list)


def elves_concert(elf_list: list["Elf"]) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list["Dwarf"]) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()
