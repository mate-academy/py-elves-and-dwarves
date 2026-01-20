from __future__ import annotations
from abc import ABC, abstractmethod


class Player(ABC):
    """Abstract base class for all players."""

    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Return player's info string."""
        pass
