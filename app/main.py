def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    # for dwarf in dwarves:
    print("\n".join([f"{dwarf.nickname} is eating "
                     f"{dwarf._favourite_dish}" for dwarf in dwarves]))
