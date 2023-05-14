from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    calculate_total_rating = 0
    for races in team:
        if type(races).__name__ == "Druid":
            calculate_total_rating += len(races.favourite_spell)
        elif type(races).__name__ == "ElfRanger":
            calculate_total_rating += 3 * races.bow_level
        elif type(races).__name__ == "DwarfWarrior":
            calculate_total_rating += races.hummer_level + 4
        elif type(races).__name__ == "DwarfBlacksmith":
            calculate_total_rating += races.skill_level
        elif races == []:
            calculate_total_rating = 0
    return calculate_total_rating


def elves_concert(elves: list[Elf]) -> int:
    for races in elves:
        print(f"{races.nickname} is playing a song on the "
              f"{races.musical_instrument}")


def play_elf_song(elves: list) -> int:
    print(f"{elves.nickname} is playing a song on the "
          f"{elves.musical_instrument}")


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> int:
    for races in dwarves:
        print(f"{races.nickname} is eating {races.favourite_dish}")


def eat_favourite_dish(dwarves: list) -> int:
    print(f"{dwarves.nickname} is eating {dwarves.favourite_dish}")
