import collections

Card = collections.namedtuple("Card", ["rank", "suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = "spades hearts clubs diamonds".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

c = Card('A', 'B')
print(c)
deck = FrenchDeck()
print(len(deck))

print(deck[0], deck[-1])

for card in deck:
    print(card)

print(deck[12::13])

deck_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
