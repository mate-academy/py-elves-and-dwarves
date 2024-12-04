from abc import ABC, abstractmethod


class Player(ABC):
    """Базовый класс для всех игроков."""

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
