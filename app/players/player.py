from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        return self.get_rating()

    @abstractmethod
    def player_info(self) -> str:
        return self.player_info()
