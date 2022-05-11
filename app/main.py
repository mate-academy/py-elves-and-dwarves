# from app.players.elves.elf_ranger import ElfRanger
# from app.players.elves.druid import Druid
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
#

def calculate_team_total_rating(heros: list):
    return sum([hero.get_rating() for hero in heros])


def elves_concert(elfs: list):
    for elf in elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list):
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
