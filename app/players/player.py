from abc import ABC, abstractmethod
from typing import Any


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> Any:
        pass

    @abstractmethod
    def player_info(self) -> Any:
        pass
