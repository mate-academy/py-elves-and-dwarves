from app.players.player import Player
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players: list) -> int:
    return sum([player.get_rating() for player in players])


def elves_concert(elves: list) -> None:
    [elf.play_elf_song() for elf in elves]


def feast_of_the_dwarves(dwarves: list) -> None:
    [dwarf.eat_favourite_dish() for dwarf in dwarves]


if __name__ == "__main__":
    player = Player("Thiddeal")
    dwarf = Dwarf("Thiddeal", "French Fries")
    dwarf_blacksmith = DwarfBlacksmith("Thiddeal", "French Fries", 3)
    dwarf_warrior = DwarfWarrior("Thiddeal", "French Fries", 3)
    druid = Druid("Thiddeal", "French Fries", "aaa")
    elf = Elf("Thiddeal", "French Fries")
    elf_ranger = ElfRanger("Thiddeal", "French Fries")
