from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str) -> None:
        self.nickname = name

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
