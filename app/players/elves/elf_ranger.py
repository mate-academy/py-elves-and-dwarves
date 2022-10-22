from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 nickname: str,
                 musical_instrument: str,
                 bow_level: int) -> None:
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def player_info(self) -> str:
        return f"Elf ranger {self.nickname}. " \
               f"{self.nickname} has bow of the {self._bow_level} level"

    def get_rating(self) -> int:
        return 3 * self._bow_level


if __name__ == "__main__":
    ranger = ElfRanger(
        nickname="Nardual Chaekian",
        musical_instrument="flute",
        bow_level=7
    )
    print(ranger.get_rating())
    # == 21
    print(ranger.player_info())
    # == "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level"
    print(ranger.play_elf_song())
    # "Nardual Chaekian is playing a song on the flute"
