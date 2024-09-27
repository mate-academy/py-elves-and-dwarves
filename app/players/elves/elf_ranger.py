"""
This is specific class for elf-ranger.
It inherits all the methods from Player and
Elf classes, and adds one additional method
particularly for the elf-ranger. All of player`s
instances should be created from this class, if
elf-ranger type is choosed to play with.
"""


from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            bow_level: int
    ):
        super().__init__(nickname, musical_instrument)
        self._bow_level = bow_level

    def get_rating(self):
        return self._bow_level * 3

    def player_info(self):
        return f"Elf ranger {self.nickname}. {self.nickname} has" \
               f" bow of the {self._bow_level} level"
