from .elf import Elf

class ElfRanger(Elf):
    def __init__(self, nickname: str, instrumental_music: str, bow_level: int):
        super().__init__(nickname, instrumental_music)
        self._bow_level = bow_level
    
    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level"
    
    def get_rating(self):
        return self._bow_level * 3