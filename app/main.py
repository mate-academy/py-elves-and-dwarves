from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.player import Player


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = sum(player.get_rating() for player in players)
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
