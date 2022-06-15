# -------- I used this imports for testing --------
# --- and commented them for a reason of flake8 error ---
# from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
# from app.players.dwarves.dwarf_warrior import DwarfWarrior
# from app.players.elves.elf_ranger import ElfRanger
# from app.players.elves.druid import Druid


def calculate_team_total_rating(players: list):
    return sum(player.get_rating() for player in players)


def elves_concert(players: list):
    for player in players:
        player.play_elf_song()


def feast_of_the_dwarves(players: list):
    for player in players:
        player.eat_favourite_dish()
