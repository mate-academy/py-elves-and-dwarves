def calculate_team_total_rating(ls: list) -> int:
    return sum(player.get_rating() for player in ls)


def elves_concert(ls: list) -> str:
    for elf in ls:
        elf.play_elf_song()


def feast_of_the_dwarves(ls: list) -> str:
    for dwarf in ls:
        dwarf.eat_favourite_dish()
