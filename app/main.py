from abc import ABC, abstractmethod
from typing import List

class Player(ABC):
    def __init__(self, nickname: str):
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass

def calculate_team_total_rating(players: List[Player]) -> int:
    return sum(player.get_rating() for player in players)

def elves_concert(elves: List['Elf']):
    for elf in elves:
        elf.play_elf_song()

def feast_of_the_dwarves(dwarves: List['Dwarf']):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
