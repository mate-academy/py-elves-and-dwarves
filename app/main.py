from typing import List

from players.player import Player
from players.elves.elf import Elf
from players.dwarves.dwarf import Dwarf
from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: List[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


def main() -> None:
    elf_team = [
        Druid("Nardual", "flute", "aaa"),
        ElfRanger("Rothilion", "trumpet", 33),
    ]

    dwarf_team = [
        DwarfWarrior("Thiddeal", "French Fries", 3),
        DwarfBlacksmith("Durin", "Ale Pie", 12),
    ]

    full_team = elf_team + dwarf_team

    print(f"Team total rating: {calculate_team_total_rating(full_team)}")

    print("\n--- Elves Concert ---")
    elves_concert(elf_team)

    print("\n--- Feast of the Dwarves ---")
    feast_of_the_dwarves(dwarf_team)


if __name__ == "__main__":
    main()
