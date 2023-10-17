from abc import ABC, abstractmethod


class Player(ABC):
    """
    The abstract base Player class.

    Attributes:
    __________
    nickname
        the name of the Player

    Methods:
    _______
    get_rating()
        the abstractmethod

    Player_info()
        the abstractmethod
    """
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
