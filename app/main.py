
def calculate_team_total_rating(players: list[object]) -> int:
    return sum([total_rating.get_rating() for total_rating in players])


def elves_concert(elf: list[object]) -> list:
    return [song.play_elf_song() for song in elf]


def feast_of_the_dwarves(dwarf: list[object]) -> list:
    return [favourite_dish.eat_favourite_dish() for favourite_dish in dwarf]
