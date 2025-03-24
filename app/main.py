from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    return "\n".join(str(dwarf.eat_favourite_dish()) for dwarf in dwarves)
