from abc import abstractmethod, ABC
from typing import Any


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> Any:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
