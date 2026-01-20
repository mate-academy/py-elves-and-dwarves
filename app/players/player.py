from abc import ABC, abstractmethod
from typing import Union


class Player(ABC):

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> Union[int, float]:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
