import abc


class Player(abc.ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abc.abstractmethod
    def get_rating(self) -> None:
        pass

    @abc.abstractmethod
    def player_info(self) -> None:
        pass
