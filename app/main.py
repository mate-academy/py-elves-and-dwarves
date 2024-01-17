def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elfs: list) -> list:
    return [elf.play_elf_song() for elf in elfs]


def feast_of_the_dwarves(dwarves: list) -> list:
    return [dwarf.eat_favourite_dish() for dwarf in dwarves]
