from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    # Example Test Cases
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    assert ranger.get_rating() == 21
    assert ranger.player_info() == (
        "Elf ranger Nardual Chaekian. "
        "Nardual Chaekian has bow of the 7 level"
    )
    ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute"

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    assert warrior.get_rating() == 11
    assert warrior.player_info() == (
        "Dwarf warrior Thiddeal. "
        "Thiddeal has a hummer of the 7 level"
    )
    warrior.eat_favourite_dish()  # "Thiddeal is eating French Fries"

    # Team Rating Calculation
    team = [
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
    assert calculate_team_total_rating(team) == 102  # 33 * 3 + 3

    # Elves Concert
    elves = [
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
    elves_concert(elves)

    # Feast of the Dwarves
    dwarves = [
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
    feast_of_the_dwarves(dwarves)
