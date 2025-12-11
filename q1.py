class Card:
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

class Deck:
    
    def __init__(self):
    #    self.card = tuple([Card((r, s)) for r in range(2,6) for s in range(2,6)])
        self.card=tuple(Card(rank, suit)
            for rank in range(2, 6)
            for suit in range(2, 6)
        )
    def __len__(self):
        return len(self.card)
    def __getitem__(self,position):
        return self.card[position]
    def __str__(self):
        return f"Deck({self.card})"

d=Deck()
 
print(d)
for i in d:
    print("card=",i)