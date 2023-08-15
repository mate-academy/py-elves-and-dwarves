from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: list) -> int:
    total_ratings = sum(player.get_rating() for player in players)
    return total_ratings


def elves_concert(elf_player: list) -> None:
    for elf in elf_player:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs_players: list) -> None:
    for dwarf in dwarfs_players:
        dwarf.eat_favourite_dish()

# Example usage

    elf_ranger = ElfRanger("Lego las", "Harp", 5)
    druid = Druid("Malfunction", "Flute", "Nature's Wrath")
    dwarf_warrior = DwarfWarrior("Gimli", "Roast Lamb", 8)
    dwarf_blacksmith = DwarfBlacksmith("Baling", "Dwarves Ale", 7)

    elf_players = [elf_ranger, druid]
    dwarf_players = [dwarf_warrior, dwarf_blacksmith]

    elves_concert(elf_players)
    feast_of_the_dwarves(dwarf_players)

    total_rating = calculate_team_total_rating(elf_players + dwarf_players)
    print("Total Team Rating:", total_rating)
