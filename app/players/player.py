from abc import ABC, abstractmethod


class Player(ABC):
    nickname = ""

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass
