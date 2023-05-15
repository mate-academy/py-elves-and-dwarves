from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for team_members in elves:
        print(f"{team_members.nickname} is playing a song on the "
              f"{team_members.musical_instrument}")


def play_elf_song(elves: list) -> None:
    print(
        f"{elves.nickname} is playing a song on the {elves.musical_instrument}"
    )


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


def eat_favourite_dish(dwarves: list) -> None:
    print(f"{dwarves.nickname} is eating {dwarves.favourite_dish}")
