from app.players.player import Player


def calculate_team_total_rating(team_of_elves: list[Player]) -> int:
    return sum(player_of_team.get_rating() for player_of_team in team_of_elves)


def elves_concert(choir_of_elves: list[Player]) -> None:
    for elf in choir_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(team_of_dwarves: list[Player]) -> None:
    for dwarv in team_of_dwarves:
        dwarv.eat_favourite_dish()
