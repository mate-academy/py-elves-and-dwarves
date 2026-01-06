from app.player import Player


def calculate_team_total_rating(team):
    return sum(player .values() for player  in team)

def elves_concert(elves):
    for elf in elves:
        print(elf.play_elf_song())

def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        print(dwarf.eqat_favorite_dish())