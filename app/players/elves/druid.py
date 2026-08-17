from app.players.elves.elf import Elf


class Druid(Elf):
    """Class representing a Druid character."""
    def __init__(self, nickname: str, musical_instrument: str,
                 favourite_spell: str) -> None:
        """Initialize a Druid instance.

            :param nickname: The unique nickname of the player.
            :type nickname: str
            :param musical_instrument: The instrument the druid plays.
            :type musical_instrument: str
            :param favourite_spell: The favourite spell of the druid.
            :type favourite_spell: str
        """
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        """Get the druid's rating based on favourite spell length.

            :return: The length of the favourite spell string.
            :rtype: int
        """
        return len(self._favourite_spell)

    def player_info(self) -> str:
        """Return formatted information about the druid.

            :return: Description of the druid's nickname and favourite spell.
            :rtype: str
        """
        return (f"Druid {self.nickname}. {self.nickname} has a favourite "
                f"spell: {self._favourite_spell}")
