from app.players.player import Player
from app.players.elves.elf import Elf
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


def calculate_team_total_rating(players) -> int:
    return sum([player.rating for player in players])


def elves_concert(elf: list[Elf]) -> None:
    for e in elf:
        e.play_elf_song()


elves = [
    Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
    ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
]
elves_concert(elves)











