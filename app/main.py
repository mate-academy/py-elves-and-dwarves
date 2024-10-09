from app.players.player import Player


def calculate_team_total_rating(team_lst: list[Player]) -> int:
    return sum(character.get_rating() for character in team_lst)


def elves_concert(elves: list[object]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarfs: list[object]) -> None:
    for dwarf in dwarfs:
        dwarf.eat_favourite_dish()
