def calculate_team_total_rating(players: list) -> int:
    result = sum([player.get_rating() for player in players])
    return result


def elves_concert(elfs: list) -> None:
    [elf.play_elf_song() for elf in elfs]


def feast_of_the_dwarves(dwarfs: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarfs]
