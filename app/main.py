def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> str:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
