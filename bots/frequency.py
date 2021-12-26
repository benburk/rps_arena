# type: ignore[attr-defined]
"""Frequency."""
from collections import Counter
from random import choice
from typing import Optional

from arena import BEAT, Hand


def play(last_move: Optional[Hand]) -> Hand:
    """Play opponent's most frequent move.

    :param last_move: The last move the opponent played
    :return: This bot's throw
    """
    assert hasattr(play, "counts")
    if last_move is None:
        play.counts = Counter()
        return choice(list(Hand))
    play.counts[last_move] += 1
    most_common = play.counts.most_common(1)[0][0]
    return BEAT[most_common]
