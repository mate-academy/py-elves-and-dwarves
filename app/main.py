from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: list) -> int:
    total_rating = 0
    for player in players:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    team = [
        Druid(nickname="Druid",
              musical_instrument="flute",
              favourite_spell="ABC"),
        ElfRanger(nickname="Ranger",
                  musical_instrument="trumpet",
                  bow_level=33),
    ]

    total_rating = calculate_team_total_rating(team)
    print(f"Team total rating: {total_rating}")

    elves = [
        Druid(nickname="Nardual",
              musical_instrument="flute",
              favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion",
                  musical_instrument="trumpet",
                  bow_level=33),
    ]

    print("Elves Concert:")
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(nickname="Thiddeal",
                     favourite_dish="French Fries",
                     hummer_level=3),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad",
                     hummer_level=3),
    ]

    print("Feast of the Dwarves:")
    feast_of_the_dwarves(dwarves)
