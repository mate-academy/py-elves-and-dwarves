from app.players.player import *
from app.players.elves.elf_ranger import *
from app.players.elves.druid import *


def calculate_team_total_rating(self, bow_level: int) -> int:
    print(bow_level * 3 + 3)

def elves_concert(self, list_main: str) -> int:
    return

def play_elf_song(self, list_main: str) -> int:
    return

def feast_of_the_dwarves(self, list_main: str) -> int:
    return

def eat_favourite_dish(self, list_main: str) -> int:
    return

team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
calculate_team_total_rating(team)  #== 102  # 33 * 3 + 3
