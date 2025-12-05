from __future__ import annotations

from abc import ABC, abstractmethod


class Player(ABC):
    """Base abstract class for all players."""

    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return the numeric rating of the player."""
        raise NotImplementedError

    @abstractmethod
    def player_info(self) -> str:
        """Return a human readable info string about the player."""
        raise NotImplementedError
