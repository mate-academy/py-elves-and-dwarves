from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


# Example usage
if __name__ == "__main__":
    ranger = ElfRanger("Nardual Chaekian", "flute", 7)
    warrior = DwarfWarrior("Thiddeal", "French Fries", 7)

    print(ranger.get_rating())  # 21
    print(ranger.player_info())  # Elf ranger Nardual Chaekian...
    ranger.play_elf_song()

    print(warrior.get_rating())  # 11
    print(warrior.player_info())  # Dwarf warrior Thiddeal...
    warrior.eat_favourite_dish()

    team = [
        Druid("Druid", "flute", "ABC"),
        ElfRanger("Ranger", "trumpet", 33),
    ]
    print(calculate_team_total_rating(team))  # 102

    elves = [
        Druid("Nardual", "flute", "aaa"),
        ElfRanger("Rothilion", "trumpet", 33),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior("Thiddeal", "French Fries", 3),
        DwarfWarrior("Dwarf", "Caesar Salad", 3),
    ]
    feast_of_the_dwarves(dwarves)
