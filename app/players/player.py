from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def player_info(self) -> None:
        raise NotImplementedError
