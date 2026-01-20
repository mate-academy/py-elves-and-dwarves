

def calculate_team_total_rating(team: list) -> int:
    return sum(teammate.get_rating() for teammate in team)


def elves_concert(elves: list) -> None:
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves]
