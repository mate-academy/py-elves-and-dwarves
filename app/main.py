# from app.players.player import Player
# from app.players.dwarves.dwarf import Dwarf
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
# from app.players.elves.elf import Elf
# from app.players.elves.elf_ranger import ElfRanger
# from app.players.elves.druid import Druid


def calculate_team_total_rating(players: list) -> int:
    result = 0

    for player in players:
        result += player.get_rating()

    return result


def elves_concert(elfes: list) -> None:
    for elf in elfes:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
