

class Elf(Player):
    def __init__(self, musical_instrument:str) -> None:
        self.musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")


class Dwarf(Player):
    def __init__(self, favourite_dish: str) -> None:
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self.favourite_dish}")
