#  from abc import ABC, abstractmethod

from typing import List
from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
#  from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
#  from app.players.dwarves.dwarf_warrior import DwarfWarrior
#  from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(players: List[Player]) -> int:
    result_rating = 0
    for work_player in players:
        result_rating += work_player.get_rating()
    return result_rating


def elves_concert(elfs: List[Elf]) -> None:
    for work_elfs in elfs:
        work_elfs.play_elf_song()


def feast_of_the_dwarves(dwarfs: List[Dwarf]) -> None:
    for work_dwarves in dwarfs:
        work_dwarves.eat_favourite_dish()


ranger = ElfRanger(
    nickname="Nardual Chaekian",
    musical_instrument="flute",
    bow_level=7
)
ttt = ranger.get_rating()  # == 21
ranger.player_info()  # == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute"
