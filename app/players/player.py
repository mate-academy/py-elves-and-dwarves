from abc import abstractmethod, ABC


class Player(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def payer_info(self):
        pass
