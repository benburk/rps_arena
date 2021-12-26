"""Basic bot that always plays rock."""
from typing import Optional

from arena import Hand


def play(_last_move: Optional[Hand]) -> Hand:
    """Always play rock.

    :return: This bot's throw
    """
    return Hand.ROCK
