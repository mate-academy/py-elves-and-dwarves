from abc import abstractmethod, ABC


class Player(ABC):

    nickname = ""

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass
