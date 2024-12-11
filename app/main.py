from players.elves import ElfRanger, Druid
from players.dwarves import DwarfWarrior, DwarfBlacksmith


def calculate_team_total_rating(players):
    """Calculates the sum of ratings for all players in the team."""
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves):
    """Calls play_elf_song for each Elf in the list."""
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    """Calls eat_favourite_dish for each Dwarf in the list."""
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


# Example usage
ranger = ElfRanger(
    nickname="Nardual Chaekian", musical_instrument="flute", bow_level=7
)
warrior = DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=7)

team = [Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"), ranger]
print(calculate_team_total_rating(team))  # Output: 102

elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"), ranger
]
elves_concert(elves)

dwarves = [warrior, DwarfBlacksmith(nickname="Dwarf", favourite_dish="Salad", skill_level=5)]
feast_of_the_dwarves(dwarves)