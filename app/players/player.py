# app/players/player.py
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> float:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
