from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
