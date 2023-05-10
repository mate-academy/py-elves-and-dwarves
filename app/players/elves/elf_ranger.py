from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self, bow_level: int, nickname: str, musical_instrument: str =None) -> str:
        self._bow_level = bow_level
        self.nickname = nickname
        self.musical_instrument = musical_instrument

    def player_info(self):
        print(f"Elf ranger {self.nickname}. {self.nickname} has bow of the {self._bow_level} level")

    def get_rating(self):
        print(3 * self._bow_level)

    def play_elf_song(self):
        print(f"{self.nickname} is playing a song on the {self.musical_instrument}")

#ranger = ElfRanger(
#    nickname="Nardual Chaekian",
#    musical_instrument="flute",
 #   bow_level=7
#)
#ranger.get_rating() #== 21
#ranger.player_info() #== "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
#ranger.play_elf_song()  # "Nardual Chaekian is playing a song on the flute"
