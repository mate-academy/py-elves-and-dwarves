from app.players import Player, Elf, Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    """Calculate the total rating of a team.

    :param team: A list of players.
    :type team: list[Player]
    :return: The total rating of the team.
    :rtype: int
    """
    return sum(member.get_rating() for member in team)


def elves_concert(elves: list[Elf]) -> None:
    """Make all elves in a list play a song.

    :param elves: A list of elves.
    :type elves: list[Elf]
    """
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    """Make all dwarves in a list eat their favourite dish.

    :param dwarves: A list of dwarves.
    :type dwarves: list[Dwarf]
    """
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
