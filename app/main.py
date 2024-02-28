def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        print(f"{dwarf.nickname} is eating {dwarf._favourite_dish}")
