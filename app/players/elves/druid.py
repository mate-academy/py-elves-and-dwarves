from app.elves.elf import Elf

class Druid(Elf):
    def __init__(self, nickname: str, power: int, healing_power: int):
        super().__init__(nickname, power)
        self.healing_power = healing_power

    def get_rating(self) -> int:
        return self.power + self.healing_power

    def player_info(self) -> str:
        return f"{self.nickname} is Druid with rating {self.get_rating()}"
