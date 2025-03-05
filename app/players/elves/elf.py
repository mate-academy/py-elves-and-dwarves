from app.players.player import Player


class Elf(Player):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str
                 ) -> None:
        super().__init__(nickname)
        self._musical_instrument = musical_instrument

    def play_elf_song(self) -> None:
        print(f"""{self.nickname} is playing 
        a song on the {self._musical_instrument}""")

    def get_rating(self) -> int:
        return 0

    def player_info(self) -> str:
        return f"""Elf {self.nickname} plays 
        the {self._musical_instrument}"""
