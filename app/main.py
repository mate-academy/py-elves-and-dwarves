from app.players.elves.elf import Elf


def calculate_team_total_rating(team: list) -> int:
    return sum(player.get_rating() for player in team)


def elves_concert(elves: list) -> None:
    for elf in elves:
        if isinstance(elf, Elf):
            elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> str:
    result = []
    for dwarf in dwarves:
        dish = dwarf.eat_favourite_dish()
        if dish is None:
            print(f"Warning: {dwarf.name} returned None!")
            result.append(f"{dwarf.name} has no favourite dish")
        else:
            result.append(dish)
    return "\n".join(result)


def eat_favourite_dish(self) -> str:
    if self._favourite_dish:
        return f"{self.nickname} is eating {self._favourite_dish}"
    else:
        return f"{self.nickname} has no favourite dish"

