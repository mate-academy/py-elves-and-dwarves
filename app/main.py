def calculate_team_total_rating(team):
    result_calculate = 0
    for player in team:
        result_calculate += player.get_rating()
    return result_calculate


def elves_concert(elves):
    result_elves_concert = []
    for elf in elves:
        result_elves_concert.append(elf.play_elf_song())
    return result_elves_concert


def feast_of_the_dwarves(dwarves):
    result_dwarves = []
    for dwarf in dwarves:
        result_dwarves.append(dwarf.eat_favourite_dish())
    return result_dwarves
