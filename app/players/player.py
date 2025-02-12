from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Abstract method to get the player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Abstract method to get player info."""
        pass
