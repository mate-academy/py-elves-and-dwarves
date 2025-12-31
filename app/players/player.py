from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """
        Return numerical rating for the player.
        """

    @abstractmethod
    def player_info(self) -> str:
        """
        Return human readable info about the player.
        """
