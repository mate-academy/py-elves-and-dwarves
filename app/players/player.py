from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname

    @abstractmethod
    def get_rating(self) -> int:
        pass

    @abstractmethod
    def player_info(self) -> str:
        pass

    def play_elf_song(self) -> None:
        pass

    def eat_favourite_dish(self) -> None:
        pass
