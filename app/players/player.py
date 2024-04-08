from abc import ABC, abstractmethod


class Player(ABC):
    nickname: str

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
