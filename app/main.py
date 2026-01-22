from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.player import Player
from typing import List


def calculate_team_total_rating(team: List[Player]) -> int:
    """
    Возвращает суммарный рейтинг всех игроков в команде.
    """
    return sum(player.get_rating() for player in team)


def elves_concert(elves: List[Druid | ElfRanger]) -> None:
    """
    Инициирует концерт эльфов, вызывая метод play_elf_song для каждого эльфа.
    """
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: List[DwarfWarrior | DwarfBlacksmith]
                         ) -> None:
    """
    Организует пиршество для гномов, вызывая метод
    eat_favourite_dish для каждого гнома.
    """
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    # Пример использования
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    warrior = DwarfWarrior(
        nickname="Thiddeal",
        favourite_dish="French Fries",
        hummer_level=7
    )

    team = [ranger, warrior]
    print(
        calculate_team_total_rating(team)
    )  # Ожидается: 21 + 11 = 32

    elves = [
        Druid(
            nickname="Nardual",
            musical_instrument="flute",
            favourite_spell="aaa"
        ),
        ElfRanger(
            nickname="Rothilion",
            musical_instrument="trumpet",
            bow_level=33
        ),
    ]
    elves_concert(elves)

    dwarves = [
        DwarfWarrior(
            nickname="Thiddeal",
            favourite_dish="French Fries",
            hummer_level=3
        ),
        DwarfBlacksmith(
            nickname="Dwarf",
            favourite_dish="Caesar Salad",
            skill_level=5
        ),
    ]
    feast_of_the_dwarves(dwarves)
