def calculate_team_total_rating(ls_players: list) -> int:
    return sum([i.get_rating() for i in ls_players])


def elves_concert(ls_elf: list) -> None:
    for elf in ls_elf:
        elf.play_elf_song()


def feast_of_the_dwarves(ls_dwarf: list) -> None:
    for dwarf in ls_dwarf:
        dwarf.eat_favourite_dish()
