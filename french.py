import collections
Card=collections.namedtuple('Card',['ranks','suits'])

# c=Card('7','spade')
# print(c)

class FrenchDeck:

    ranks=[]
    for i in range(2,11):
        ranks.append(i)
    ranks+=list("JQKV")
    # print(ranks)
    suits=[]
    suits+='spades diamonds clubs hearts'.split()
    # print(suits)

    def __init__(self):
        self.cards=[]
        for suits in self.suits:
            for ranks in self.ranks:
                self.cards+=[Card(ranks,suits)]
    def __len__(self):
        return len(self.cards)
    def __getitem__(self,position):
        return self.cards[position]
    def __setitem__(self,position,item):
        old_card=self.cards[position]
        self.cards[position]=Card(old_card.ranks,item)

deck=FrenchDeck()
# print(len(deck))
# print(deck[0])
# print(deck)

# from random import choice

# print(choice(deck))
# print(deck[2:3])

# for i in reversed(deck):
#     print(i)

# deck[0]="kalidas"

# for i in deck:
#     print(i)


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value=FrenchDeck.ranks.index(card.ranks)
    return rank_value*len(suit_values)+suit_values[card.suits]

for i in sorted(deck,key=spades_high):
    print(card)
