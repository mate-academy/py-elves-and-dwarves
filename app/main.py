from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.dwarves.dwarf import Dwarf


def calculate_team_total_rating(list_of_players:
                                list[Player]
                                ) -> int:
    result = 0
    for obj in list_of_players:
        result += obj.get_rating()
    return result


def elves_concert(elfs:
                  list[Elf]
                  ) -> None:
    for obj in elfs:
        obj.play_elf_song()


def feast_of_the_dwarves(dwarfs:
                         list[Dwarf]
                         ) -> None:
    for obj in dwarfs:
        obj.eat_favourite_dish()
