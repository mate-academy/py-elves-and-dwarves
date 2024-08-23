from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(
    players: list[ElfRanger, Druid, DwarfWarrior, DwarfBlacksmith]
) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list[Druid, ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[DwarfBlacksmith, DwarfWarrior]) -> None:
    for dwarv in dwarves:
        dwarv.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian", musical_instrument="flute", bow_level=7
    )
    warrior = DwarfWarrior(
        nickname="Thiddeal", favourite_dish="French Fries", hummer_level=7
    )

    team = [ranger, warrior]
    print(calculate_team_total_rating(team))  # 21 + 11 = 32

    elves = [
        Druid(
            nickname="Nardual",
            musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(
            nickname="Thiddeal",
            favourite_dish="French Fries",
            hummer_level=3
        ),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad",
                     hummer_level=3
                     ),
    ]
    feast_of_the_dwarves(dwarves)
