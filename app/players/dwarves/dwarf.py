from abc import ABC
from app.players.player import Player


class Dwarf(Player, ABC):
    def __init__(self, nickname: str, favourite_dish: str):
        self.nickname = nickname
        self.favourite_dish = favourite_dish

    def eat_favourite_dish(self):
        print(f"{self.nickname} is eating {self.favourite_dish}")
