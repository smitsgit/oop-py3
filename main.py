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


class AceCard(Card):
    def _points(self):
        return 1, 11


class FaceCard(Card):
    def _points(self):
        return 10, 10


def card(rank, suit):
    """
    There are two ways to have factory in Python
    1. We define a function that creates objects of Required classes
    2. We define a class that has methods for creating objects.
       In languages such as Java, a full factory is required cause
       the language doesn't support standalone functions

       We can now build cards more easily using Rank and Suit
       We have encapsulated construction issues into single factory function,
       allowing and application to be built without knowing precisely, how the
       class hierarchy and polymorphic design works
    """
    if rank == 1:
        return AceCard('A', suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
        name = {11: 'J', 12: 'Q', 13: 'K'}[rank]
        return FaceCard(name, suit)
    else:
        raise ValueError('Rank out of Range')


def main():
    cards: List[Card] = [AceCard('A', '♠'), NumberCard('5', '♠'), NumberCard('7', '♠')]
    # for card in cards:
    #     print(card._points())

    Club, Dimond, Spade, Heart = Suit('club', '♣'), Suit('dimond', '◆'), Suit('spade', '♠'), Suit('heart', '♥')

    cardlst: List[Card] = [AceCard(1, Spade), NumberCard(5, Club), NumberCard(7, Heart), FaceCard(10, Dimond)]
    for card in cardlst:
        print(card._points())
        print(card.suit.symbol)


if __name__ == '__main__':
    main()
