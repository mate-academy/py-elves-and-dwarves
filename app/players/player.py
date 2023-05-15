from abc import ABC, abstractmethod


class Player(ABC):
    @property
    @abstractmethod
    def nickname(self) -> None:
        pass

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass
