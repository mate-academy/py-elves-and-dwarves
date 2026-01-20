def calculate_team_total_rating(player: list) -> int:
    return sum(player.get_rating() for player in player)


def elves_concert(elf: list) -> None:
    for el in elf:
        el.play_elf_song()


def feast_of_the_dwarves(dwarf: list) -> None:
    for dwa in dwarf:
        dwa.eat_favourite_dish()
