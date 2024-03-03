
def calculate_team_total_rating(players_group: list) -> int:
    return sum(teammate.get_rafting() for teammate in players_group)


def elves_concert(elfs_group: list) -> None:
    for elf in elfs_group:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_group: list) -> None:
    for dwarf in dwarfs_group:
        dwarf.eat_favourite_dish()
