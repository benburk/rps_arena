"""Rock paper scissors arena.

Arena framework allows for
- reflection for loading bot files by name
- bot implementation with minimal boilerplate
"""
import itertools
from collections import defaultdict
from enum import Enum, auto
from pprint import pprint
from typing import Callable, Optional


class Hand(Enum):
    """Different hands a player can throw."""

    ROCK = 0
    PAPER = auto()
    SCISSORS = auto()


BEAT = {Hand.ROCK: Hand.PAPER, Hand.PAPER: Hand.SCISSORS, Hand.SCISSORS: Hand.ROCK}


class Bot:
    """Class for holding the information of a bot
    the code of the bot is loaded as a string, compiled, and executed

    scope holds the variables, in our case it is only the
    function 'play(move)'
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.scope: dict[str, Callable[[Optional[Hand]], Hand]] = {}
        self.reset()

    def reset(self) -> None:
        """Initialize the bot by executing the script."""
        with open(f"bots/{self.name}.py", encoding="utf8") as file:
            # read the file as string, and execute it
            # adds all local variables to the dictionary self.scope
            exec(file.read(), self.scope)  # pylint: disable=exec-used

    def get_move(self, last_move: Optional[Hand]) -> Hand:
        """Ask the bot for a move, given the last_move
        played of the last round

        :param last_move: The last move the opponent played
        :return: This bot's throw
        """
        return self.scope["play"](last_move)


N_ROUNDS = 1000


def play_match(player1: Bot, player2: Bot, n_rounds: int) -> list[int]:
    """Play a match of n_rounds between two bots.

    :param player1: Player 1
    :param player2: Player 2
    :param n_rounds: The number of rounds to play
    :return: A triple of (draws, player 1 wins, player 2 wins)
    """
    hand1 = hand2 = None
    score = [0, 0, 0]  # tie, player1, player2
    for _ in range(n_rounds):
        hand1, hand2 = player1.get_move(hand2), player2.get_move(hand1)
        score[hand1.value - hand2.value] += 1
    return score


def play_matches(bot_names: list[str]) -> defaultdict[str, int]:
    """Play matches.

    :param bot_names: The names of the bots to play against each other
    :return: The number of wins each player had
    """
    leaderboard: defaultdict[str, int] = defaultdict(int)

    bots = [Bot(name) for name in bot_names]
    pairings = itertools.combinations(bots, 2)
    for player1, player2 in pairings:
        print(f"{player1.name} vs {player2.name}")
        score = play_match(player1, player2, 1000)
        leaderboard[player1.name] += score[1]
        leaderboard[player2.name] += score[2]
        print(f"result: {score}")

    return leaderboard


def main() -> None:
    """Main method."""
    bot_names = ["always_rock", "random", "beat_last", "frequency"]
    leaderboard = play_matches(bot_names)

    pprint(leaderboard)


if __name__ == "__main__":
    main()
