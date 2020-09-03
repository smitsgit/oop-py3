"""
Ideally it will be good to have Suit attributes Immutable.
Cause this is acting as a constant
"""


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return f"Suit({self.name}, {self.symbol})"
