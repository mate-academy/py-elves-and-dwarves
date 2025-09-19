from typing import List

from .players.dwarves.dwarf import Dwarf
from .players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from .players.dwarves.dwarf_warrior import DwarfWarrior
from .players.elves.druid import Druid
from .players.elves.elf import Elf
from .players.elves.elf_ranger import ElfRanger
from .players.player import Player


def calculate_team_total_rating(team: List[Player]) -> int:
    total_rating = 0
    for player in team:
        total_rating += player.get_rating()
    return total_rating


def elves_concert(elves: List[Elf]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[Dwarf]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


# Código de exemplo para verificação, conforme fornecido no documento [1]
if __name__ == "__main__":
    # Instâncias para os exemplos
    druid_1 = Druid(
        nickname="Druid", musical_instrument="flute", favourite_spell="ABC"
    )
    elf_ranger_1 = ElfRanger(
        nickname="Ranger", musical_instrument="trumpet", bow_level=33
    )
    druid_2 = Druid(
        nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"
    )
    elf_ranger_2 = ElfRanger(
        nickname="Rothilion", musical_instrument="trumpet", bow_level=33
    )
    dwarf_warrior_1 = DwarfWarrior(
        nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3
    )
    dwarf_warrior_2 = DwarfWarrior(
        nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3
    )
    # Instância extra para garantir que DwarfBlacksmith seja usado
    dwarf_blacksmith_1 = DwarfBlacksmith(
        nickname="Balin", favourite_dish="Mutton", skill_level=15
    )

    # Preenchendo a lista 'team'
    team = [druid_1, elf_ranger_1]
    print(f"Team total rating: {calculate_team_total_rating(team)}")
    print("-" * 20)

    # Preenchendo a lista 'elves'
    elves = [druid_2, elf_ranger_2]
    print("Elves concert:")
    elves_concert(elves)
    print("-" * 20)

    # Preenchendo a lista 'dwarves'
    dwarves = [dwarf_warrior_1, dwarf_warrior_2, dwarf_blacksmith_1]
    print("Feast of the dwarves:")
    feast_of_the_dwarves(dwarves)
