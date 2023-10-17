from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """
    ElfRanger class.

    Attributes:
    ___________
    nickname
        the name of the Elf
    musical_instrument
        the Elf's musical instrument
    bow_level
        the Elf's bow level

    Methods:
    _______
    get_rating()
        returns the bow level rating

    player_info()
        displays a message about the Elf Ranger

    play_elf_song()
        displays a message about playing song
    """
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        super().__init__(
            nickname=nickname,
            musical_instrument=musical_instrument
        )
        self._bow_level = bow_level

    def get_rating(self) -> int:
        """
        Returns the bow level rating.
        :return: int
        """
        return 3 * self._bow_level

    def player_info(self) -> str:
        """
        Displays a message about Elf Ranger
        :return:
        """
        return (f"Elf ranger {self.nickname}. "
                f"{self.nickname} has bow of the {self._bow_level} level")
