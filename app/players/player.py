from abc import ABC, abstractmethod


class Player(ABC):

    nicknames = []

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
        Player.nicknames.extend([nickname])

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
