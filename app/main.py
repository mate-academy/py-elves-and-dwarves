from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


def main() -> None:
    elf1 = ElfRanger("Nardual", "flute", 7)
    elf2 = Druid("Elenaril", "flute", "abrakadabra")
    dwarf1 = DwarfWarrior("Thiddeal", "French Fries", 7)
    dwarf2 = DwarfBlacksmith("Thiddeal", "French Fries", 14)

    team = [elf1, elf2, dwarf1, dwarf2]

    elves_concert([elf1, elf2])
    feast_of_the_dwarves([dwarf1, dwarf2])
    print("Team rating:", calculate_team_total_rating(team))


if __name__ == "__main__":
    main()
