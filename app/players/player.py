from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating() -> None:
        pass

    @abstractmethod
    def player_info() -> None:
        pass
