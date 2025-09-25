from players.player import Player
from players.elves.elf import Elf
from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf import Dwarf
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger("Nardual Chaekian", "flute", 7)
    print(ranger.player_info())
    print(ranger.get_rating())
    ranger.play_elf_song()

    druid = Druid("Elwin", "harp", "Fireball")
    print(druid.player_info())
    print(druid.get_rating())
    druid.play_elf_song()

    warrior = DwarfWarrior("Thiddeal", "French Fries", 7)
    print(warrior.player_info())
    print(warrior.get_rating())
    warrior.eat_favourite_dish()

    blacksmith = DwarfBlacksmith("Borin", "Stew", 10)
    print(blacksmith.player_info())
    print(blacksmith.get_rating())
    blacksmith.eat_favourite_dish()

    team = [ranger, druid, warrior, blacksmith]
    print("Total team rating:", calculate_team_total_rating(team))

    elves = [ranger, druid]
    print("\nElves concert:")
    elves_concert(elves)

    dwarves = [warrior, blacksmith]
    print("\nFeast of the dwarves:")
    feast_of_the_dwarves(dwarves)
