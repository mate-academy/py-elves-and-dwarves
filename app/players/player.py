from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Return player's rating."""
        pass

    @abstractmethod
    def player_info(self) -> str:
        """Return string with player info."""
        pass

    @abstractmethod
    def declared(self) -> None:
        """Dummy abstract method required by task."""
        pass
