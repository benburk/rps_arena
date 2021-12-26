"""Beat last bot."""
from random import choice
from typing import Optional

from arena import BEAT, Hand


def play(last_move: Optional[Hand]) -> Hand:
    """Play opponent's last move.

    :param last_move: The last move the opponent played
    :return: This bot's throw
    """
    return choice(list(Hand)) if last_move is None else BEAT[last_move]
