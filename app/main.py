# from app.players.player import Player
# from app.players.elves.elf import Elf
# from app.players.elves.druid import Druid
# from app.players.elves.elf_ranger import ElfRanger
# from app.players.dwarves.dwarf import Dwarf
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
#

def calculate_team_total_rating(team: list) -> int:
    result = 0
    for player in team:
        result += player.get_rating()
    return result


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
