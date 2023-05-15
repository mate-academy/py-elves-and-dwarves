from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(self, nickname: str, favourite_spell: str,
                 musical_instrument: str) -> str:
        self.favourite_spell = favourite_spell
        self.nickname = nickname
        self.musical_instrument = musical_instrument

    def get_rating(self) -> int:
        return len(self.favourite_spell)

    def player_info(self) -> str:
        return f"Druid {self.nickname}. {self.nickname} " \
               f"has a favourite spell: {self.favourite_spell}"

    def play_elf_song(self) -> None:
        print(f"{self.nickname} is playing a song on the "
              f"{self.musical_instrument}")
