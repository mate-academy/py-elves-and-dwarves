from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract base class for all players in the game."""

    def __init__(self, nickname: str) -> None:
        """Initialize a Player instance.

            :param nickname: The unique nickname of the player.
            :type nickname: str
        """
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Calculate and return the player's power rating.

            :return: The rating score of the player.
            :rtype: int
        """
        ...

    @abstractmethod
    def player_info(self) -> str:
        """Return formatted information about the player.

            :return: Information describing the player.
            :rtype: str
        """
        ...
