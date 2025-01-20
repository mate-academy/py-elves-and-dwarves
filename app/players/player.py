from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name: str) -> None:
        self.nickname = name

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
