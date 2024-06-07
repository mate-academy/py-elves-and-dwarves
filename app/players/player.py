from abc import ABC, abstractmethod


class Player(ABC):
    players = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        self.players.append(self)

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
