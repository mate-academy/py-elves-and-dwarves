from abc import ABC, abstractmethod


class Player(ABC):
    """A base class for all players."""

    def __init__(self, nickname: str) -> None:
        """Initialize the player.

        :param nickname: The player's nickname.
        :type nickname: str
        """
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Get the player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Get the player's info."""
        pass
