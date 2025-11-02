from abc import abstractmethod, ABC


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> None:
        pass

    @abstractmethod
    def player_info(self) -> None:
        pass



class Elf(Player):
    def __init__(self, nickname: str, musical_instrument: str) -> None:
        super().__init__(nickname)
        self._musical_instrument  = musical_instrument

    def gat_rating(self):
        ...

    def player_info(self) -> None:
        ...

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname)
        self._favourite_dish = favourite_dish

    def gat_rating(self):
        ...

    def player_info(self) -> None:
        ...

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

