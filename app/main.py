"""
This main.py module contains three function. Each
of them takes a list of instances of players (both
elves and dwarves), and performs some of their methods.
Methods can print or return string, or return an integer,
to provide some information about a player.
"""


def calculate_team_total_rating(players):
    return sum(
        [
            player.get_rating() for player in players
        ]
    )


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
