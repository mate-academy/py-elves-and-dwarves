from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return player's rating."""
        raise NotImplementedError

    @abstractmethod
    def player_info(self) -> str:
        """Return short player description."""
        raise NotImplementedError
