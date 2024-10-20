from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(players: list[Player]) -> int:
    total_rating = sum(player.get_rating() for player in players)
    return total_rating


def elves_concert(elves: list[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[Dwarf]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    players = [
        ElfRanger("Legolas", "Harp", 10),
        Druid("Elrond", "Flute", "Healing Spell"),
        DwarfWarrior("Gimli", "Meat", 8),
        DwarfBlacksmith("Balin", "Ale", 7)
    ]
    print("Total team rating:", calculate_team_total_rating(players))

    elves = [ElfRanger("Legolas", "Harp", 10),
             Druid("Elrond", "Flute", "Healing Spell")]
    elves_concert(elves)

    dwarfs = [DwarfWarrior("Gimli", "Meat", 8),
              DwarfBlacksmith("Balin", "Ale", 7)]
    feast_of_the_dwarves(dwarfs)
