from players.elves.elf import Elf


class Druid(Elf):
    # `Druid` should be a child of `Elf`.
    # Its `__init__` method should take one additional parameter:
    # `favourite_spell` - the text of the favourite spell.
    # The `__init__` method should store it in the protected attribute.
    def __init__(self, nickname: str,
                 musical_instrument: str, favourite_spell: str) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> int:
        # `get_rating` method should return:
        # * length of `favourite_spell` for `Druid`
        return len(self._favourite_spell)

    def player_info(self) -> str:
        # * `"Druid {nickname}. {nickname} has
        # a favourite spell: {favourite_spell}"` for `Druid` instances
        return (f"Druid {self.nickname}. {self.nickname} "
                f"has a favourite spell: {self._favourite_spell}")

