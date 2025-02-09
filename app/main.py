from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(team: list[Player]) -> int:
    return sum(member.get_rating()
               for member in team if isinstance(member, Player))
    # for team_member in team:
    #     if isinstance(team_member, Player):
    #         total_rating += team_member.get_rating()


def elves_concert(elves: list[Elf]) -> str:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[Dwarf]) -> str:
    for dwarf in dwarves:
        if isinstance(dwarf, Dwarf):
            dwarf.eat_favourite_dish()
