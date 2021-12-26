"""Random bot."""
from random import choice
from typing import Optional

from arena import Hand


def play(_last_move: Optional[Hand]) -> Hand:
    """Play random move.

    :return: This bot's throw
    """
    return choice(list(Hand))
