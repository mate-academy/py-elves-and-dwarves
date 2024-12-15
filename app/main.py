from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if nick == "__main__":
    # Example players
    elf_ranger = ElfRanger("Legolas", "flute", 7)
    druid = Druid("Elrond", "harp", "Healing Light")
    dwarf_warrior = DwarfWarrior("Gimli", "meat stew", 10)
    dwarf_blacksmith = DwarfBlacksmith("Thorin", "roast pork", 8)

    # Test team functions
    players = [elf_ranger, druid, dwarf_warrior, dwarf_blacksmith]
    print("Team Total Rating:", calculate_team_total_rating(players))

    # Elves concert
    elves_concert([elf_ranger, druid])

    # Feast of the Dwarves
    feast_of_the_dwarves([dwarf_warrior, dwarf_blacksmith])
