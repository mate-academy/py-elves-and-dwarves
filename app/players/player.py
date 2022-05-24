from abc import ABC, abstractmethod


class Player(ABC):
    nickname = []

    def __init__(self, nickname: str):
        self.nickname = nickname
        Player.nickname.append(nickname)

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
