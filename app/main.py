from players.player import Player
from players.dwarves.dwarf import Dwarf
from players.elves.elf import Elf
from players.elves.elf_ranger import ElfRanger
from players.elves.druid import Druid
from players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    return sum(player.get_rating() for player in list_of_players)


def elves_concert(list_of_elves: list[Elf]) -> None:
    for elf in list_of_elves:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarf in list_of_dwarves:
        dwarf.eat_favourite_dish()


if __name__ == '__main__':

    team = [
        Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
    ]
    calculate_team_total_rating(team)

    elves = [
        Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)
