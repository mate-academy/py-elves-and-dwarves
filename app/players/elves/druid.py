from app.players.elves.elf import Elf


class Druid(Elf):
    """A class to represent a druid."""

    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ) -> None:
        """Initialize the druid.

        :param nickname: The druid's nickname.
        :type nickname: str
        :param musical_instrument: The druid's musical instrument.
        :type musical_instrument: str
        :param favourite_spell: The druid's favourite spell.
        :type favourite_spell: str
        """
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def player_info(self) -> str:
        """Get the druid's info.

        :return: The druid's info.
        :rtype: str
        """
        return (
            f"Druid {self.nickname}. "
            f"{self.nickname} has a favourite spell: "
            f"{self._favourite_spell}"
        )

    def get_rating(self) -> int:
        """Get the druid's rating.

        :return: The druid's rating.
        :rtype: int
        """
        return len(self._favourite_spell)
