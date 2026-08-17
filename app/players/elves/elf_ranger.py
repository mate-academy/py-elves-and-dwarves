from app.players.elves.elf import Elf


class ElfRanger(Elf):
    """Class representing an Elf Ranger character."""
    def __init__(self, nickname: str, musical_instrument: str,
                 bow_level: int) -> None:
        """Initialize an ElfRanger instance.

            :param nickname: The unique nickname of the player.
            :type nickname: str
            :param musical_instrument: The instrument the elf plays.
            :type musical_instrument: str
            :param bow_level: The level of the ranger's bow.
            :type bow_level: int
        """
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self) -> int:
        """Get the ranger's rating based on bow level.

            :return: The rating calculated from bow level multiplied by 3.
            :rtype: int
        """
        return self._bow_level * 3

    def player_info(self) -> str:
        """Return formatted information about the elf ranger.

            :return: Description of the ranger's nickname and bow level.
            :rtype: str
        """
        return (f"Elf ranger {self.nickname}. {self.nickname} has bow of the "
                f"{self._bow_level} level")
