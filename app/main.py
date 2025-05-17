from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nick_name: str) -> None:
        self.nickname = nick_name

    @abstractmethod
    def get_rating(self):
        pass

    @abstractmethod
    def player_info(self):
        pass


class Elf(Player):
    def __init__(self, nick_name: str, musical_instrument: str) -> None:
        super().__init__(nick_name)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the {self._musical_instrument}")

    def get_rating(self):
        pass

    def player_info(self):
        pass


class Dwarf(Player):
    def __init__(self, nick_name: str, favourite_dish: str) -> None:
        super().__init__(self, nick_name)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")

    def get_rating(self):
        pass

    def player_info(self):
        pass
