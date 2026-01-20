from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_warrior import DwarfWarrior
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players):
    return sum(player.get_rating() for player in players)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(nickname="Nardual Chaekian", musical_instrument="flute", bow_level=7)
    druid = Druid(nickname="Nardual", musical_instrument="harp", favourite_spell="Healing Wind")
    warrior = DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=7)
    blacksmith = DwarfBlacksmith(nickname="Borin", favourite_dish="Steak", skill_level=10)

    team = [ranger, druid, warrior, blacksmith]
    print(f"Total team rating: {calculate_team_total_rating(team)}")

    elves = [ranger, druid]
    elves_concert(elves)

    dwarves = [warrior, blacksmith]
    feast_of_the_dwarves(dwarves)