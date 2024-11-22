from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


# Function to calculate the total rating of a team
def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


# Function to host an elves' concert
def elves_concert(elves: list):
    for elf in elves:
        elf.play_elf_song()


# Function to host a feast for dwarves
def feast_of_the_dwarves(dwarves: list):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


# Example usage
if __name__ == "__main__":
    # Example team for total rating calculation
    team = [
        Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
    ]
    print(calculate_team_total_rating(team))  # 102

    # Example elves concert
    elves = [
        Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ]
    elves_concert(elves)  # "Nardual is playing a song on the flute" and "Rothilion is playing a song on the trumpet"

    # Example feast for dwarves
    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)  # "Thiddeal is eating French Fries" and "Dwarf is eating Caesar Salad"
