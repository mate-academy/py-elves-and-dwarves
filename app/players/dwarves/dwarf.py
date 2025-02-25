from app.players.player import Player


class Dwarf(Player):
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        self.nickname = nickname          # Зберігаємо нікнейм
        self._favourite_dish = favourite_dish  # Зберігаємо улюблену страву

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
