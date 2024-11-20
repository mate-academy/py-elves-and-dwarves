from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(team):
    return sum(player.get_rating() for player in team)


def elves_concert(elves):
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves):
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()


if __name__ == "__main__":
    team = [
        Druid(nickname="Nardual", musical_instrument="флейта", favourite_spell="aaa"),
        ElfRanger(nickname="Rothilion", musical_instrument="труба", bow_level=33),
        DwarfWarrior(nickname="Thiddeal", favourite_dish="Картопля фрі", hummer_level=3),
        DwarfBlacksmith(nickname="Balin", favourite_dish="Цезар Салат", skill_level=5),
    ]

    print(f"Total team rating: {calculate_team_total_rating(team)}")
    elves_concert([player for player in team if isinstance(player, Druid)
                   or isinstance(player, ElfRanger)])
    feast_of_the_dwarves(
        [player for player in team if isinstance(player, DwarfWarrior)
         or isinstance(player, DwarfBlacksmith)])
