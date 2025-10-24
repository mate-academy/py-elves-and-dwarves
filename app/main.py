from app.players.dwarves.dwarf import Dwarf


def main() -> None:
    dwarf = Dwarf("Thorin", "Roast Mutton")
    dwarf.eat_favourite_dish()
    print(dwarf.player_info())
    print("Rating:", dwarf.get_rating())


def calculate_team_total_rating(players: list) -> int:
    return sum(player.get_rating() for player in players)


def elves_concert(elves: list) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
