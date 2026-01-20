from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, nickname: str) -> None:
        self.nickname = nickname

    @abstractmethod
    def get_rating(self) -> int:
        """Returns the player's rating."""
        pass  # Явно указываем, что метод пустой

    @abstractmethod
    def player_info(self) -> str:
        """Returns player information."""
        pass  # Добавили явный pass
