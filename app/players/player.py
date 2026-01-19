"""
The base class should be the Player class,
which should have a single nickname attribute,
where the player's name will be stored.
It must also have two empty abstract methods get_rating,
player_info, declared,
thus we guarantee that all players in our universe will have them defined.
"""
from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def player_info(self) -> None:
        pass

    @abstractmethod
    def get_rating(self) -> None:
        pass
