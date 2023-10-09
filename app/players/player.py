from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: int) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    def player_info(self) -> None:
        pass
