# from app.players.player import Player
# from app.players.elves.elf import Elf
# from app.players.elves.druid import Druid
# from app.players.elves.elf_ranger import ElfRanger
# from app.players.dwarves.dwarf import Dwarf
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
# from app.players.dwarves.dwarf_warrior import DwarfWarrior

def calculate_team_total_rating(players: list) -> int:
    total = 0
    for player in players:
        total += player.get_rating()
    return total


def elves_concert(elves: list) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> str:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
