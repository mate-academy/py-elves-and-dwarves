def calculate_team_total_rating(players: list) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elf_singers: list):
    return [song.play_elf_song() for song in elf_singers]


def feast_of_the_dwarves(dwarf_eat: list):
    return [dish.eat_favourite_dish() for dish in dwarf_eat]
