from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        self.nickname = nickname
        self._musical_instrument = musical_instrument

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
