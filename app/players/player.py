from abc import ABC, abstractmethod


class Player(ABC):
    nickname: str

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
