from app.players.player import Player


class Elf(Player):
    """Intermediate class for Elf race."""
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ) -> None:
        """Initialize an Elf with a nickname and a musical_instrument."""
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        """Print a message about the elf playing a song."""
        print(f"{self.nickname} is playing a song"
              f" on the {self._musical_instrument}")
