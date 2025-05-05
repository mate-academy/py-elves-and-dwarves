def calculate_team_total_rating(team: list) -> int:
    team_ratings = []
    for team_player in team:
        team_ratings.append(team.get_rating())
        return sum(team_ratings)


def elves_concert(elves: list) -> str:
    for elf in elves:
        return (
            f"{elf.nickname} is playing a song on the"
            f"{elf._musical_instrument}"
        )


def feast_of_the_dwarves(dwarves: list) -> str:
    for dwarf in dwarves:
        return f"{dwarf.nickname} is eating {dwarf._favourite_dish}"
