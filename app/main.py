from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(teams: list) -> int:
    total_rating = 0
    for player in teams:
        total_rating += player.get_rating()

    return total_rating


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves_list: list) -> None:
    for dwarf in dwarves_list:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    team = [
        Druid(
            nickname="Druid", musical_instrument="flute", favourite_spell="ABC"
        ),
        ElfRanger(
            nickname="Ranger", musical_instrument="trumpet", bow_level=33
        ),
    ]
    elves = [
        Druid(
            nickname="Nardual", musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion", musical_instrument="trumpet", bow_level=33
        ),
    ]
    dwarves = [
        DwarfWarrior(
            nickname="Thiddeal", favourite_dish="French Fries", hammer_level=3
        ),
        DwarfWarrior(
            nickname="Dwarf", favourite_dish="Caesar Salad", hammer_level=3
        ),
    ]

    calculate_team_total_rating(team)
    elves_concert(elves)
    feast_of_the_dwarves(dwarves)
