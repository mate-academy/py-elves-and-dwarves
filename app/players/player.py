from __future__ import annotations

from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def player_info(self) -> str:
        raise NotImplementedError
