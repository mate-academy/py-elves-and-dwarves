from __future__ import annotations

if __name__ == "__main__":
    from players.player import Player
    from players.elves.elf import Elf
    from players.dwarves.dwarf import Dwarf
    from players.dwarves.dwarf_warrior import DwarfWarrior
else:
    from app.players.player import Player
    from app.players.elves.elf import Elf
    from app.players.dwarves.dwarf import Dwarf
    from app.players.dwarves.dwarf_warrior import DwarfWarrior


def calculate_team_total_rating(players: list[Player]) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(players: list[Elf]) -> None:
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list[Dwarf]) -> None:
    for player in players:
        player.eat_favourite_dish()


# Code test block
if __name__ == "__main__":
    dwarves = [
        DwarfWarrior(nickname="Thiddeal",
                     favourite_dish="French Fries", hummer_level=3),
        DwarfWarrior(nickname="Dwarf",
                     favourite_dish="Caesar Salad", hummer_level=3),
    ]
    feast_of_the_dwarves(dwarves)
