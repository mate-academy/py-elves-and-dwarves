from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(team: List[Player]) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    print(f"Рейтинг рейнджера: {ranger.get_rating()}")
    print(f"Інформація про рейнджера: {ranger.player_info()}")
    ranger.play_elf_song()
    print("-" * 20)

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    print(f"Рейтинг воїна: {warrior.get_rating()}")
    print(f"Інформація про воїна: {warrior.player_info()}")
    warrior.eat_favourite_dish()
    print("-" * 20)

    team = [
        Druid(nickname="Druid",
              musical_instrument="flute",
              favourite_spell="ABC"),
        ElfRanger(nickname="Ranger",
                  musical_instrument="trumpet",
                  bow_level=33),
    ]
    total_rating = calculate_team_total_rating(team)
    print(f"Загальний рейтинг команди: {total_rating}")
    print("-" * 20)

    elves = [
        Druid(nickname="Nardual",
              musical_instrument="flute",
              favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion",
                  musical_instrument="trumpet",
                  bow_level=33),
    ]
    print("Концерт ельфів:")
    elves_concert(elves)
    print("-" * 20)

    dwarves = [
        DwarfWarrior(nickname="Thiddeal",
                     favourite_dish="French Fries",
                     hummer_level=3),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad",
                     hummer_level=3),
    ]
    print("Бенкет гномів:")
    feast_of_the_dwarves(dwarves)
