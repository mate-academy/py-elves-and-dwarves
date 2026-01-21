from typing import List

from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: List[Elf]) -> None:
    print("\n-- Elves Concert Start --")
    for elf in elves:
        elf.play_elf_song()
    print("-- Elves Concert End --\n")


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    print("\n-- Dwarves Feast Start --")
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
    print("-- Dwarves Feast End --\n")


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    druid = Druid(
        nickname="Elara Meadowlight",
        musical_instrument="harp",
        favourite_spell="Entangling Roots"
    )
    warrior = DwarfWarrior(
        nickname="Thiddeal Stonebeard",
        favourite_dish="Roasted Boar",
        hummer_level=10
    )
    blacksmith = DwarfBlacksmith(
        nickname="Borin Anvilhand",
        favourite_dish="Mutton Stew",
        skill_level=15
    )

    print("--- Individual Tests ---")
    print(f"Ranger Info: {ranger.player_info()}")
    print(f"Ranger Rating: {ranger.get_rating()}")
    ranger.play_elf_song()

    print(f"\nWarrior Info: {warrior.player_info()}")
    print(f"Warrior Rating: {warrior.get_rating()}")
    warrior.eat_favourite_dish()

    print("\n--- Team Tests ---")
    team = [ranger, druid, warrior, blacksmith]
    total_rating = calculate_team_total_rating(team)
    print(f"Team Total Rating: {total_rating}")

    elves = [ranger, druid]
    elves_concert(elves)

    dwarves = [warrior, blacksmith]
    feast_of_the_dwarves(dwarves)

    # --- Prompt Verification (Lines Reformatted) ---
    print("\n--- Prompt Verification ---")
    ranger_check = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    ranger_rating = ranger_check.get_rating()
    ranger_rating_correct = ranger_rating == 21
    print(
        f"Ranger Rating Check: {ranger_rating} == 21 -> "
        f"{ranger_rating_correct}"
    )

    ranger_info = ranger_check.player_info()
    expected_ranger_info = (
        "Elf ranger Nardual Chaekian. "
        "Nardual Chaekian has bow of the 7 level"
    )
    ranger_info_correct = ranger_info == expected_ranger_info
    print(
        f"Ranger Info Check: '{ranger_info}' == '...' -> "
        f"{ranger_info_correct}"
    )
    ranger_check.play_elf_song()

    warrior_check = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    warrior_rating = warrior_check.get_rating()
    warrior_rating_correct = warrior_rating == 11
    print(
        f"Warrior Rating Check: {warrior_rating} == 11 -> "
        f"{warrior_rating_correct}"
    )

    warrior_info = warrior_check.player_info()
    expected_warrior_info = (
        "Dwarf warrior Thiddeal. "
        "Thiddeal has a hummer of the 7 level"
    )
    warrior_info_correct = warrior_info == expected_warrior_info
    print(
        f"Warrior Info Check: '{warrior_info}' == '...' -> "
        f"{warrior_info_correct}"
    )
    warrior_check.eat_favourite_dish()

    team_check = [
        Druid(
            nickname="Druid",
            musical_instrument="flute",
            favourite_spell="ABC"
        ),
        ElfRanger(
            nickname="Ranger",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    team_rating = calculate_team_total_rating(team_check)
    team_rating_correct = team_rating == 102
    print(
        f"Team Rating Check: {team_rating} == 102 -> "
        f"{team_rating_correct}"
    )

    elves_check = [
        Druid(
            nickname="Nardual",
            musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    elves_concert(elves_check)

    dwarves_check = [
        DwarfWarrior(
            nickname="Thiddeal",
            favourite_dish="French Fries",
            hummer_level=3
        ),
        DwarfWarrior(
            nickname="Dwarf",
            favourite_dish="Caesar Salad",
            hummer_level=3
        ),
    ]
    feast_of_the_dwarves(dwarves_check)
