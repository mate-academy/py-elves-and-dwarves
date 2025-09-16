from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:   # int
        pass

    @abstractmethod
    def player_info(self) -> None:    # str
        pass
