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

    ranger = ElfRanger("Nardual Chaekian", "flute", 7)

    print(ranger.get_rating())
    print(ranger.player_info()) == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
