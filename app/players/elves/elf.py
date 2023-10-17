from app.players.player import Player


class Elf(Player):
    """
    The abstract Elf class.

    Attributes:
    ___________
    nickname
        the name of the Elf
    musical_instrument
        the Elf's musical instrument

    Methods:
    _______
    get_rating()
        the abstractmethod

    player_info()
        the abstractmethod

    play_elf_song()
        displays a message about playing song
    """
    def __init__(
            self,
            nickname: str,
            musical_instrument: str
    ) -> None:
        super().__init__(nickname=nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        """
        Displays a message about playing song.
        :return: None
        """
        print(
            f"{self.nickname} is playing a song on the "
            f"{self._musical_instrument}"
        )
