import inspect
import io
from contextlib import redirect_stdout

import pytest

from app import main
from app.main import calculate_team_total_rating, elves_concert, feast_of_the_dwarves
from app.players.dwarves.dwarf import Dwarf
from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf import Elf
from app.players.elves.elf_ranger import ElfRanger
from app.players.player import Player


@pytest.mark.parametrize(
    "class_,methods",
    [
        (Player, ["get_rating", "player_info"]),
        (Elf, ["get_rating", "player_info", "play_elf_song"]),
        (ElfRanger, ["get_rating", "player_info", "play_elf_song"]),
        (Druid, ["get_rating", "player_info", "play_elf_song"]),
        (Dwarf, ["get_rating", "player_info", "eat_favourite_dish"]),
        (DwarfWarrior, ["get_rating", "player_info", "eat_favourite_dish"]),
        (DwarfBlacksmith, ["get_rating", "player_info", "eat_favourite_dish"]),
    ],
)
def test_classes_should_have_corresponding_methods(class_, methods):
    for method in methods:
        assert (
                hasattr(class_, method)
        ), f"Class '{class_.__name__}' should have method {method}"


@pytest.mark.parametrize(
    "class_",
    [
        Player, Elf, Dwarf,
    ]
)
def test_classes_should_be_abstract(class_):
    assert inspect.isabstract(class_), (
        f"Class '{class_.__name__}' should be abstract"
    )


@pytest.mark.parametrize(
    "class_",
    [
        ElfRanger, Druid, DwarfWarrior, DwarfBlacksmith,
    ]
)
def test_classes_should_not_be_abstract(class_):
    assert not inspect.isabstract(class_), (
        f"Class '{class_.__name__}' shouldn't be abstract"
    )


@pytest.mark.parametrize(
    "class_,methods",
    [
        (Elf, ["get_rating", "player_info"]),
        (Dwarf, ["get_rating", "player_info"]),
    ],
)
def test_abstract_methods_should_not_be_redefined(class_, methods):
    for method in methods:
        assert (
            getattr(class_, method) is getattr(Player, method)
        ), f"Class '{class_.__name__}' should not redefine " \
           f"abstract method '{method}'"


@pytest.mark.parametrize(
    "nickname,musical_instrument,bow_level,rating,song,player_info",
    [
        (
            "Nardual Chaekian",
            "flute",
            7,
            21,
            "Nardual Chaekian is playing a song on the flute\n",
            "Elf ranger Nardual Chaekian. Nardual Chaekian has bow of the 7 level",
        ),
        (
            "Rothilion Yinfiel",
            "trumpet",
            5,
            15,
            "Rothilion Yinfiel is playing a song on the trumpet\n",
            "Elf ranger Rothilion Yinfiel. Rothilion Yinfiel has bow of the 5 level",
        ),
    ]
)
def test_elf_ranger_class(
    nickname,
    musical_instrument,
    bow_level,
    rating,
    song,
    player_info,
):
    ranger = ElfRanger(
        nickname=nickname,
        musical_instrument=musical_instrument,
        bow_level=bow_level
    )
    assert ranger.get_rating() == rating
    assert ranger.player_info() == player_info
    f = io.StringIO()
    with redirect_stdout(f):
        ranger.play_elf_song()
    assert f.getvalue() == song


@pytest.mark.parametrize(
    "nickname,musical_instrument,favourite_spell,rating,song,player_info",
    [
        (
            "Elenaril Paxina",
            "flute",
            "abrakadabra",
            11,
            "Elenaril Paxina is playing a song on the flute\n",
            "Druid Elenaril Paxina. Elenaril Paxina has a favourite spell: abrakadabra",
        ),
        (
            "Althidon Perzumin",
            "trumpet",
            "sim-sim",
            7,
            "Althidon Perzumin is playing a song on the trumpet\n",
            "Druid Althidon Perzumin. Althidon Perzumin has a favourite spell: sim-sim",
        ),
    ]
)
def test_druid_class(
    nickname,
    musical_instrument,
    favourite_spell,
    rating,
    song,
    player_info,
):
    ranger = Druid(
        nickname=nickname,
        musical_instrument=musical_instrument,
        favourite_spell=favourite_spell
    )
    assert ranger.get_rating() == rating
    assert ranger.player_info() == player_info
    f = io.StringIO()
    with redirect_stdout(f):
        ranger.play_elf_song()
    assert f.getvalue() == song


@pytest.mark.parametrize(
    "nickname,favourite_dish,hummer_level,rating,eating_message,player_info",
    [
        (
            "Thiddeal",
            "French Fries",
            7,
            11,
            "Thiddeal is eating French Fries\n",
            "Dwarf warrior Thiddeal. Thiddeal has a hummer of the 7 level",
        ),
        (
            "Dwarf",
            "Caesar Salad",
            10,
            14,
            "Dwarf is eating Caesar Salad\n",
            "Dwarf warrior Dwarf. Dwarf has a hummer of the 10 level",
        ),
    ]
)
def test_dwarf_warrior_class(
    nickname,
    favourite_dish,
    hummer_level,
    rating,
    eating_message,
    player_info,
):
    warrior = DwarfWarrior(
        nickname=nickname,
        favourite_dish=favourite_dish,
        hummer_level=hummer_level
    )
    assert warrior.get_rating() == rating
    assert warrior.player_info() == player_info
    f = io.StringIO()
    with redirect_stdout(f):
        warrior.eat_favourite_dish()
    assert f.getvalue() == eating_message


@pytest.mark.parametrize(
    "nickname,favourite_dish,skill_level,rating,eating_message,player_info",
    [
        (
            "Thiddeal",
            "French Fries",
            14,
            14,
            "Thiddeal is eating French Fries\n",
            "Dwarf blacksmith Thiddeal with skill of the 14 level",
        ),
        (
            "Dwarf",
            "Caesar Salad",
            8,
            8,
            "Dwarf is eating Caesar Salad\n",
            "Dwarf blacksmith Dwarf with skill of the 8 level",
        ),
    ]
)
def test_dwarf_blacksmith_class(
    nickname,
    favourite_dish,
    skill_level,
    rating,
    eating_message,
    player_info,
):
    blacksmith = DwarfBlacksmith(
        nickname=nickname,
        favourite_dish=favourite_dish,
        skill_level=skill_level
    )
    assert blacksmith.get_rating() == rating
    assert blacksmith.player_info() == player_info
    f = io.StringIO()
    with redirect_stdout(f):
        blacksmith.eat_favourite_dish()
    assert f.getvalue() == eating_message


@pytest.mark.parametrize(
    "team,rating",
    [
        ([],  0),
        (
            [Druid(nickname="Druid", musical_instrument="", favourite_spell="aaa")],
            3
        ),
        (
            [
                Druid(nickname="Druid", musical_instrument="", favourite_spell="aaa"),
                ElfRanger(nickname="Ranger", musical_instrument="", bow_level=33),
            ],
            102
        ),
        (
            [
                DwarfWarrior(nickname="Dwarf", favourite_dish="", hummer_level=6),
                ElfRanger(nickname="Ranger", musical_instrument="", bow_level=2),
            ],
            16
        ),
        (
            [
                DwarfWarrior(nickname="Dwarf", favourite_dish="", hummer_level=6),
                ElfRanger(nickname="Ranger1", musical_instrument="", bow_level=2),
                ElfRanger(nickname="Ranger2", musical_instrument="", bow_level=6),
                DwarfBlacksmith(nickname="DwarfBlacksmith", favourite_dish="", skill_level=10),
            ],
            44
        ),
    ]
)
def test_calculate_team_total_rating(team, rating):
    assert calculate_team_total_rating(team) == rating


@pytest.mark.parametrize(
    "elves,songs",
    [
        (
            [
                Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
                ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
            ],
            (
                "Nardual is playing a song on the flute\n"
                "Rothilion is playing a song on the trumpet\n"
            )
        ),
        (
            [
                Druid(nickname="Nardual", musical_instrument="flute", favourite_spell="aaa"),
                ElfRanger(nickname="Rothilion", musical_instrument="trumpet", bow_level=33),
                Druid(nickname="Faridal", musical_instrument="flute", favourite_spell="aaa"),
            ],
            (
                "Nardual is playing a song on the flute\n"
                "Rothilion is playing a song on the trumpet\n"
                "Faridal is playing a song on the flute\n"
            )
        ),
    ]
)
def test_elves_concert(elves, songs):
    f = io.StringIO()
    with redirect_stdout(f):
        elves_concert(elves)
    assert f.getvalue() == songs


@pytest.mark.parametrize(
    "dwarves,feast_output",
    [
        (
            [
                DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
                DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
            ],
            (
                "Thiddeal is eating French Fries\n"
                "Dwarf is eating Caesar Salad\n"
            )
        ),
        (
                [
                    DwarfWarrior(nickname="Thiddeal", favourite_dish="French Fries", hummer_level=3),
                    DwarfWarrior(nickname="Dwarf", favourite_dish="Caesar Salad", hummer_level=3),
                    DwarfWarrior(nickname="Dwarf2", favourite_dish="French Fries", hummer_level=3),
                ],
                (
                        "Thiddeal is eating French Fries\n"
                        "Dwarf is eating Caesar Salad\n"
                        "Dwarf2 is eating French Fries\n"
                )
        )
    ]
)
def test_feast_of_the_dwarves(dwarves, feast_output):
    f = io.StringIO()
    with redirect_stdout(f):
        feast_of_the_dwarves(dwarves)
    assert f.getvalue() == feast_output


@pytest.mark.parametrize(
    "class_",
    [
        ElfRanger, Druid, DwarfWarrior, DwarfBlacksmith
    ],
)
def test_some_classes_not_subclass_of_abc(class_):
    lines = inspect.getsource(class_)
    assert "ABC" not in lines


def test_comment_deleted():
    lines = inspect.getsource(main)
    assert "# write your code here" not in lines
