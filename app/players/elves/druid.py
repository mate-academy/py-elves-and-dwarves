"""
This is specific class for druid.
It inherits all the methods from Player and
Elf classes, and adds one additional method
particularly for the druid. All of player`s
instances should be created from this class, if
druid type is choosed to play with.
"""


from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str,
            favourite_spell: str
    ):
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self):
        return len(self._favourite_spell)

    def player_info(self):
        return f"Druid {self.nickname}. {self.nickname} has" \
               f" a favourite spell: {self._favourite_spell}"
