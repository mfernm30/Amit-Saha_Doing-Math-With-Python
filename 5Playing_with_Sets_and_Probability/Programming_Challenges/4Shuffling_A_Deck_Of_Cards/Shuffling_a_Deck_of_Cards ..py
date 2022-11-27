from card import Card
import random

if __name__ == '__main__':
    deck = []
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    letter_ranks = ['J', 'Q', 'K']
    
    for s in suits:
        for n in range(1,11):
            deck.append(Card(s, n))
        for l in letter_ranks:
            deck.append(Card(s, l))

    for c in deck:
        print(c.rank, c.suit)

    random.shuffle(deck)
    print("\nDeck shuffle: ")
    
    for c in deck:
        print(c.rank, c.suit)
    
    print("Deck length: ", len(deck))