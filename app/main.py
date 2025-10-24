from players.dwarves.dwarf import Dwarf


def main() -> None:
    dwarf = Dwarf("Thorin", "Roast Mutton")
    dwarf.eat_favourite_dish()
    print(dwarf.player_info())
    print("Rating:", dwarf.get_rating())
