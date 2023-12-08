from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    def get_rating(self) -> int:
        pass

    def player_info(self) -> str:
        pass
