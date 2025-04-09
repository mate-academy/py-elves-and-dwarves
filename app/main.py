from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlackSmith


def calculate_team_total_rating(team_list: list[Player]):
    sum_ratings = 0
    for team in team_list:
        sum_ratings += team.get_rating()
    return sum_ratings

def elves_concert(elf_list: list[Elf]):
    play_list = [elf.play_elf_song() for elf in elf_list]
    return "\n".join(str(play) for play in play_list if play is not None)

def feast_of_the_dwarves(dwarf_list: list[Dwarf]):
    dish_list = [dwarf.eat_favourite_dish() for dwarf in dwarf_list]
    return "\n".join(str(dish) for dish in dish_list if dish is not None)


ranger = ElfRanger(
    nickname="Nardual Chaekian",
    musical_instrument="flute",
    bow_level=7
)
print(ranger.get_rating())# == 21
print(ranger.player_info())# == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
print(ranger.play_elf_song())  # "Nardual Chaekian is playing a song on the flute"

warrior = DwarfWarrior(
    nickname="Thiddeal",
    favourite_dish="French Fries",
    hummer_level=7
)
print(warrior.get_rating())# == 11
print(warrior.player_info())# == "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level"
print(warrior.eat_favourite_dish())  # "Thiddeal is eating French Fries"

team = [
    Druid(nickname="Druid", musical_instrument="flute", favourite_spell="ABC"),
    ElfRanger(nickname="Ranger", musical_instrument="trumpet", bow_level=33),
]
print(calculate_team_total_rating(team))# == 102  # 33 * 3 + 3

elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
]
print(elves_concert(elves))
# "Nardual is playing a song on the flute"
# "Rothilion is playing a song on the trumpet"

dwarves = [
    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
]
print(feast_of_the_dwarves(dwarves))
# "Thiddeal is eating French Fries"
# "Dwarf is eating Caesar Salad"
