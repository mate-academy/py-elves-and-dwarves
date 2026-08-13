from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith

def calculate_team_total_rating(players_list: list[Player]) -> int:
    return sum(player.get_rating() for player in players_list)

def elves_concert(elves_list: list[Player]) -> None:
    for player in elves_list:
        if isinstance(player, Elf):
            player.play_elf_song()

def feast_of_the_dwarves(dwarves_list: list[Player]) -> None:
    for player in dwarves_list:
        if isinstance(player, Dwarf):
            player.eat_favourite_dish()



if __name__ == '__main__':
    team = [
        Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
        ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
    ]

    print(calculate_team_total_rating(team))

    elves = [
        Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
    ]
    print(elves_concert(elves))

    dwarves = [
        DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
    ]
    print(feast_of_the_dwarves(dwarves))