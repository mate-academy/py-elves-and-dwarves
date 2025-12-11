from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> float:
        pass

    @abstractmethod
    def player_info(self) -> dict:
        pass

    @abstractmethod
    def declared(self) -> bool:
        pass
