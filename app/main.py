def calculate_team_total_rating(players: list) -> int:
    rating_team = 0
    for player in players:
        rating_team += player.get_rating()
    return rating_team


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
