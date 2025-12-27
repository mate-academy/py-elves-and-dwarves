from abc import ABC, abstractmethod


class Player(ABC):
    nickname = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        Player.nickname.append(self.nickname)

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
