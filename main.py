from typing import List
from suits import Suit

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class Ace(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


def main():
    cards: List[Card] = [Ace(1, '♠'), NumberCard(5, '♠'), NumberCard(7, '♠')]
    # for card in cards:
    #     print(card._points())

    Club, Dimond, Spade, Heart = Suit('club', '♣'), Suit('dimond', '◆'), Suit('spade', '♠'), Suit('heart', '♥')

    cardlst: List[Card] = [Ace(1, Spade), NumberCard(5, Club), NumberCard(7, Heart), FaceCard(10, Dimond)]
    for card in cardlst:
        print(card._points())
        print(card.suit.symbol)


if __name__ == '__main__':
    main()
