from players.player import Player


class Elf(Player):
    # All elves like playing songs so
    # `Elf` `__init__` method should take an additional argument
    # `musical_instrument` -  and stored it in the **protected** attribute.
    # Also, it should have a method
    # `play_elf_song` that should print the following string:
    # `"{nickname} is playing a song on the {musical_instrument}"`
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> str:
        print(f"{self.nickname} is "
              f"playing a song on the {self._musical_instrument}")
