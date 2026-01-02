from elf import Elf

class Druid(Elf):
    def __init__(self, nickname: str, instrumental_music: str, favourite_spell: str):
        super().__init__(nickname, instrumental_music)
        self.favourite_spell = favourite_spell
    
    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} has a favourite spell: {self.favourite_spell}"

    def get_rating(self):
        return len(self.favourite_spell)