from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract base class for all players in the universe."""

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return the player's numeric rating."""

    @abstractmethod
    def player_info(self) -> str:
        """Return a human-readable description of the player."""
