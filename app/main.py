from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(list_of_players: list[Player]) -> int:
    team_total_rating_list = [
        player.get_rating() for player in list_of_players
    ]
    return sum(team_total_rating_list)


def elves_concert(list_of_elfs: list[Elf]) -> None:
    for elf in list_of_elfs:
        elf.play_elf_song()


def feast_of_the_dwarves(list_of_dwarves: list[Dwarf]) -> None:
    for dwarve in list_of_dwarves:
        dwarve.eat_favourite_dish()


team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
print(calculate_team_total_rating(team))
