from app.players.elves.elf_ranger import ElfRanger
from app.players.elves.druid import Druid
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith


def calculate_team_total_rating(list_of_player: list) -> total_rating:
    total_rating = 0
    for play in list_of_player:
        total_rating += play.get_rating()
    return total_rating
# return sum(player.get_rating() for player in players)


def elves_concert(list_of_elf: list) -> None:
    for elf_member in list_of_elf:
        if (isinstance(elf_member, ElfRanger)
                or isinstance(elf_member, Druid)):
            elf_member.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        if (isinstance(dwarf, DwarfWarrior)
                or isinstance(dwarf, DwarfBlacksmith)):
            dwarf.eat_favourite_dish()


if __name__ == "__main__":
    # Example usage
    ranger = ElfRanger(nickname="Nardual Chaekian"
                       , musical_instrument="flute"
                       , bow_level=7)
    warrior = DwarfWarrior(nickname="Thiddeal"
                           , favourite_dish="French Fries"
                           , hummer_level=7)
    druid = Druid(nickname="Fandral"
                  , musical_instrument="harp"
                  , favourite_spell="Healing Rain")
    blacksmith = DwarfBlacksmith(nickname="Durin"
                                 , favourite_dish="Ale"
                                 , skill_level=10)

    # Testing individual players
    print(ranger.player_info())
    print(warrior.player_info())
    print(druid.player_info())
    print(blacksmith.player_info())
