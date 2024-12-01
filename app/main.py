

def calculate_team_total_rating(team: list):
    rating = 0
    for member in team:
        print(member)
        rating += member.get_rating()
    return rating


def elves_concert(musicians: list):
    for musician in musicians:
        musician.play_elf_song()


def feast_of_the_dwarves(gluttons: list):
    for glutton in gluttons:
        glutton.eat_favourite_dish()
