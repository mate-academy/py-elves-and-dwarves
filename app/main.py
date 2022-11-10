

def calculate_team_total_rating(teams: list) -> int:
    summary = 0
    for player in teams:
        summary += int(player.get_rating())
    return summary


def elves_concert(actors: list) -> None:
    for actor in actors:
        actor.play_elf_song()


def feast_of_the_dwarves(dishes: list) -> None:
    for dish in dishes:
        dish.eat_favourite_dish()
