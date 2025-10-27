from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, nickname: str, race: str, power: int):
        self.nickname = nickname
        self.race = race
        self.power = power

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
