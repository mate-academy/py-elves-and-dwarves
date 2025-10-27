from app.elves.elf import Elf

class ElfRanger(Elf):
    def get_rating(self) -> int:
        return self.power * 2

    def player_info(self) -> str:
        return f"{self.nickname} is Elf Ranger with rating {self.get_rating()}"
