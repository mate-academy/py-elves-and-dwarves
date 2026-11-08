from abc import ABC, abstractmethod


class Player(ABC):

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
