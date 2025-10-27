from players.elves.elf_ranger import ElfRanger
from app.elves.druid import Druid
from app.dwarves.dwarf_warrior import DwarfWarrior
from app.dwarves.dwarf_blacksmith import DwarfBlacksmith

def main():
    players = [
        ElfRanger("Legolas", 50),
        Druid("Elrond", 40, 20),
        DwarfWarrior("Gimli", 60),
        DwarfBlacksmith("Thorin", 55, 30),
    ]

    for player in players:
        print(player.player_info())


if __name__ == "__main__":
    main()
