def calculate_team_total_rating(players):
    total_rating = sum(player.get_rating() for player in players)
    return total_rating


def elves_concert(elves) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()