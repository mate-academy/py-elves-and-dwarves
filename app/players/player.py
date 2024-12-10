from abc import ABC, abstractmethod


class Player(ABC):
    def __int__(self, nickname: str) -> None:
        pass

    @abstractmethod
    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass
