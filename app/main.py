from app.players.player import Player


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(person.get_rating() for person in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
