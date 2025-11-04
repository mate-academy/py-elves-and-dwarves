from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )

    print(ranger.get_rating())
    print(ranger.player_info())
    ranger.play_elf_song()

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )

    print(warrior.get_rating())
    print(warrior.player_info())
    warrior.eat_favourite_dish()

    team = [
        Druid(nickname="Druid", musical_instrument="flute",
              favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet",
                  bow_level=33),
    ]
    print(calculate_team_total_rating(team))

    elves = [
        Druid(nickname="Nardual", musical_instrument="flute",
              favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet",
                  bow_level=33),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries",
                     hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad",
                     hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)
