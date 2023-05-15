from app.players.dwarves.dwarf import Dwarf
from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    if team is None:
        return 0
    else:
        return sum(
            team_member.get_rating() for team_member in team if
            type(team_member).__name__ in ["Druid", "ElfRanger",
                                           "DwarfWarrior", "DwarfBlacksmith"]
        )


def elves_concert(elves: list[Elf]) -> None:
    for team_members in elves:
        print(f"{team_members.nickname} is playing a song on the "
              f"{team_members.musical_instrument}")


def play_elf_song(elves: list) -> None:
    print(
        f"{elves.nickname} is playing a song on the {elves.musical_instrument}"
    )


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for team_members in dwarves:
        print(
            f"{team_members.nickname} is eating {team_members.favourite_dish}"
        )


def eat_favourite_dish(dwarves: list) -> None:
    print(f"{dwarves.nickname} is eating {dwarves.favourite_dish}")
