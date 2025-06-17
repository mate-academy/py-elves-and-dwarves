from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(
        team: list
) -> int:
    result = 0
    if team is not False:
        for player in team:
            result += player.get_rating()
    return result


def elves_concert(elves: list) -> None:
    if elves is not False:
        for elf in elves:
            elf.play_elf_song()


def feast_of_the_dwarves(dwarf: list) -> None:
    if dwarf is not False:
        for dwar in dwarf:
            dwar.eat_favorite_dish()
