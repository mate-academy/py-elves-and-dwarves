from typing import List
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(team: List[object]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[object]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[object]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger("Nardual Chaekian", "flute", 7)
    print(ranger.get_rating())  # 21
    print(ranger.player_info())
    ranger.play_elf_song()

    warrior = DwarfWarrior("Thiddeal", "French Fries", 7)
    print(warrior.get_rating())  # 11
    print(warrior.player_info())
    warrior.eat_favourite_dish()

    team = [
        Druid("Druid", "flute", "ABC"),
        ElfRanger("Ranger", "trumpet", 33),
    ]
    print(calculate_team_total_rating(team))  # 102

    elves = [
        Druid("Nardual", "flute", "aaa"),
        ElfRanger("Rothilion", "trumpet", 33),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior("Thiddeal", "French Fries", 3),
        DwarfWarrior("Dwarf", "Caesar Salad", 3),
    ]
    feast_of_the_dwarves(dwarves)
