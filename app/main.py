def calculate_team_total_rating(players: list) -> int | float:
    team_rating = []
    for i in players:
        team_rating.append(i.get_rating())
    return sum(team_rating)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
