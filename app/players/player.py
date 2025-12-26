from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass

    def __repr__(self) -> str:
        return ", ".join(f"{key!r}{value!r}"
                         for key, value in self.__dict__.values())
