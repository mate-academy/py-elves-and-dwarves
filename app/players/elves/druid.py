from app.players.elves.elf import Elf


class Druid(Elf):
    """
    Druid class

     Attributes:
    ___________
    nickname
        the name of the Elf
    musical_instrument
        the Elf's musical instrument
    favourite_spell
        the Druid's favorite spell

    Methods:
    _______
    get_rating()
        returns the favorite spell length

    player_info()
        displays a message about the Druid

    play_elf_song()
        displays a message about playing song
    """
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        """
        Returns the length of the 'favorite spell'.
        :return: int
        """
        return len(self._favourite_spell)

    def player_info(self) -> str:
        """
        Displays a message about the Druid.
        :return: None
        """
        return (f"Druid {self.nickname}. "
                f"{self.nickname} has a favourite spell: "
                f"{self._favourite_spell}")
