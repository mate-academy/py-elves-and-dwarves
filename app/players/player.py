from abc import ABC, abstractmethod


# main clas
class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        # abstract method for player

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
