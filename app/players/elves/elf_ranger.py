from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """A class to represent an elf ranger."""

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ) -> None:
        """Initialize the elf ranger.

        :param nickname: The elf ranger's nickname.
        :type nickname: str
        :param musical_instrument: The elf ranger's musical instrument.
        :type musical_instrument: str
        :param bow_level: The elf ranger's bow level.
        :type bow_level: int
        """
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        """Get the elf ranger's info.

        :return: The elf ranger's info.
        :rtype: str
        """
        return (
            f"Elf ranger {self.nickname}. "
            f"{self.nickname} has bow of the {self._bow_level} level"
        )

    def get_rating(self) -> int:
        """Get the elf ranger's rating.

        :return: The elf ranger's rating.
        :rtype: int
        """
        return self._bow_level * 3
