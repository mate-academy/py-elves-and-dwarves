from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players):
    return sum(player.get_rating() for player in players)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger("Nardual Chaekian", "flute", 7)
    print(ranger.get_rating())
    print(ranger.player_info())
    ranger.play_elf_song()

    warrior = DwarfWarrior("Thiddeal", "French Fries", 7)
    print(warrior.get_rating())
    print(warrior.player_info())
    warrior.eat_favourite_dish()
