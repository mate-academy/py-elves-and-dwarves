from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass
