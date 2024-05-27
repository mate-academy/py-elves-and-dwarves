def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elfs: list) -> None:
    for elve in elfs:
        elve.play_elf_song()


def feast_of_the_dwarves(dwarfs: list) -> None:
    for dwarve in dwarfs:
        dwarve.eat_favourite_dish()
