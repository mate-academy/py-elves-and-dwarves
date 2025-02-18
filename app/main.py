from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elf_list: list) -> None:
    for elf in elf_list:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarf_list: list) -> None:
    for dwarf in dwarf_list:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    print(ranger.get_rating() == 21)
    print(ranger.player_info() == "Elf ranger"
                                  " Nardual Chaekian. Nardual Chaekian "
                                  "has bow of the 7 level"
          )
    ranger.play_elf_song()

    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )
    print(warrior.get_rating() == 11)
    print(warrior.player_info() == "Dwarf warrior"
                                   " Thiddeal. Thiddeal has a hummer"
                                   " of the 7 level"
          )
    warrior.eat_favourite_dish()

    team_example = [
        Druid(nickname="Druid",
              musical_instrument="flute",
              favourite_spell="ABC"
              ),
        ElfRanger(nickname="Ranger",
                  musical_instrument="trumpet",
                  bow_level=33
                  ),
    ]
    print(calculate_team_total_rating(team_example) == 102)

    elves_example = [
        Druid(nickname="Nardual",
              musical_instrument="flute",
              favourite_spell="aaa"
              ),
        ElfRanger(nickname="Rothilion",
                  musical_instrument="trumpet",
                  bow_level=33
                  ),
    ]
    elves_concert(elves_example)

    dwarves_example = [
        DwarfWarrior(nickname="Thiddeal",
                     favourite_dish="French Fries",
                     hummer_level=3
                     ),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad",
                     hummer_level=3
                     ),
    ]
    feast_of_the_dwarves(dwarves_example)
