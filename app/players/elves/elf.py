from player import Player


class Elf(Player):
    def __init__(self, name: str, musical_instrument: str) -> None:
        super().__init(name)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        first_part = f"{self.name} is playing a song on"
        second_part = f" the {self._musical_instrument}"
        print(first_part + second_part)
