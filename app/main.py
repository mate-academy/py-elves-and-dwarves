def calculate_team_total_rating(player: list) -> int:
    return sum([player.get_rating() for player in player])


def elves_concert(elf: list) -> None:
    [el.play_elf_song() for el in elf]


def feast_of_the_dwarves(dwarf: list) -> None:
    [dwa.eat_favourite_dish() for dwa in dwarf]
