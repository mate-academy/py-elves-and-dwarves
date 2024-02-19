from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elve in elves:
        elve.play_elf_song()


def feast_of_the_dwarves(dishes: list) -> None:
    for dish in dishes:
        dish.eat_favourite_dish()
