from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(ls:
                                list[ElfRanger | Druid
                                     | DwarfWarrior | DwarfBlacksmith]
                                ) -> int:
    result = 0
    for obj in ls:
        result += obj.get_rating()
    return result


def elves_concert(ls:
                  list[ElfRanger | Druid]
                  ) -> None:
    for obj in ls:
        if isinstance(obj, (ElfRanger, Druid)):
            obj.play_elf_song()


def feast_of_the_dwarves(ls:
                         list[DwarfBlacksmith | DwarfWarrior]
                         ) -> None:
    for obj in ls:
        if isinstance(obj, (DwarfWarrior, DwarfBlacksmith)):
            obj.eat_favourite_dish()
