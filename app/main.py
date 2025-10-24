from players.dwarves.dwarf import Dwarf

if __name__ == "__main__":
    dwarf = Dwarf("Thorin", "Roast Mutton")
    dwarf.eat_favourite_dish()
    print(dwarf.player_info())
    print("Rating:", dwarf.get_rating())
