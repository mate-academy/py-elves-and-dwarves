from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    calculate_total_rating = []
    for races in team:
        if type(races).__name__ == "Druid":
            calculate_total_rating.append(races.get_rating())
        elif type(races).__name__ == "ElfRanger":
            calculate_total_rating.append(races.get_rating())
        elif type(races).__name__ == "DwarfWarrior":
            calculate_total_rating.append(races.get_rating())
        elif type(races).__name__ == "DwarfBlacksmith":
            calculate_total_rating.append(races.get_rating())
        elif races is None:
            return 0
    return sum(calculate_total_rating)


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
