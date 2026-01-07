from abc import ABC, abstractmethod

@abstractmethod
class Player(ABC):
    nickname = ""

    def __init__(self, nickname):
        self.nickname = nickname

    def get_rating(self):
        pass

    def player_info(self):
        pass