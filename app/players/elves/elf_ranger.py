class ElfRanger(Elf):
    def __init__(self, bow_level: int) -> str:
        self._bow_level = bow_level

    def player_info(self, nickname, bow_level):
        return f"Elf ranger {nickname}. {nickname} has bow of the {bow_level} level"

    def get_rating(self, bow_level):
        return 3 * bow_level
