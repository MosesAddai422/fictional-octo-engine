# <cards.py>
# Author: <Moses Addai>
# <04/24/2022>

# Simple text-based class for playing cards

from random import randrange

import random

class Card:
    ranks = list("23456789TJQKA")
    suits = list("CDHS")

    def __init__(self, rank, suit):
        

        if not(rank in Card.ranks):
            raise ValueError("Inappropriate rank")
        if not(suit in Card.suits):
            raise ValueError("Inappropriate suit")
        
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.suit == "H":
            suitchr = chr(9829)
        elif self.suit == "D":
            suitchr = chr(9830)
        elif self.suit == "S":
            suitchr =  chr(9824)
        else:
            suitchr = chr(9827)
        
        return self.rank + suitchr
        

class Deck:
    
    #Deck contains all cards in the Game
    def __init__(self):
        ranks = Card.ranks
        suits = Card.suits
    
        self.thedeck = []

        self.count = 0
        for i in suits:
            for v in ranks:
                self.thedeck.append(Card(v,i))
                self.count = self.count+1


    def getDeck(self):
        #brings out the deck of cards
        return self.thedeck
    

    def shuffle(self):
        #shuffles the order of the cards
        remcopy = self.thedeck.copy()
        for i in range(len(self.thedeck)):
            random = randrange(len(remcopy))
            self.thedeck[i] = remcopy[random]
            remcopy.pop(random)
        return remcopy
    
    
    def __str__(self):
        #prints out the code with a space before and after each card
        for i in self.thedeck:
            out = " " +i+ " "
                       
        return out
        

    def cardsLeft(self):
        #brings out the number of remaining cards
        return(self.count - 10)
    
   
    def dealOneCard(self):
        #produces the top row of the deck
    
        return self.thedeck.pop()
     

class BlackjackHand:
    #n = 2
    
    def __init__(self):
        hand =[]
        self.hand = hand
        
    
    def getCards(self, deck, n):
        for i in range(n):
            onecard = deck.dealOneCard()
            self.hand.append(onecard)

    def handValue(self):
        value = 0
        numace = 0
        for card in self.hand:
            if card.rank in list("KQJT"):
                value += 10
            elif card.rank in list("98765432"):
                value += int(card.rank)
            elif card.rank == "A":
                value += 1
                numace += 1

        if numace > 0:
            if value + 10 <= 21:
                value += 10

        return value
            
                
            
                

    def isBust(self):
        #status = handValue(self,chosen)

        if self.handValue() > 21:
            return True


    def revealFirstCard(self):

        
        return str(self.hand[0])
        
  
    def clear(self):

        return self.hand.clear()
       

    def __str__(self):
        out1 = ""
        for i in self.hand:
            out1 = out1 + str(i)+ " "
        return out1




def test_Card():
    """ Testing the Card class. """

    #print(Card.ranks)
    #print(Card.suits)

    for r in Card.ranks:
        for s in Card.suits:
            cardsel = Card(r,s)
            #print(cardsel)

    
  


def test_Deck():
  
    #Beginning the run

    print("Starting Deck")
    print("\n")

    vDeck = Deck()
    ct = 1
    deckroll = vDeck.getDeck()
    for j in deckroll:
        print(j, end = " ")
        if ct%13 == 0:
            print("\n")
        ct = ct + 1


    #Testing DealOneCard
    top = []
    for i in range(10):
        x = vDeck.dealOneCard()
        top.append(x)
    print("Dealt the hand:", end = "")
    for j in top:
        print("",j,end = "")
        

    #Removing the selected cards
    print("\n")
    print("The deck is now as follows:")
    print("\n")
    for p in deckroll:
        print(p, end = " ")
        if ct%13 == 0:
            print("\n")
        ct = ct + 1

    #Testing CardsLeft
    print("\n")    
    left = vDeck.cardsLeft()
    print("The deck has",left,"cards left")


    #Testing Shuffle
    shuff = vDeck.shuffle()
    print("\n")
    print("Shuffling")
    print("\n")
    ct =1
    for y in deckroll:
        print(y, end = " ")
        if ct%13 == 0:
            print("\n")
        ct = ct + 1
    
            
def test_BlackjackHand():
    #n = 2
    deck = Deck()
    #blak = 
    deck.shuffle()
  
    
    playerhand = BlackjackHand()

    #Testing getCards
    playerhand.getCards(deck, 3)
    print(playerhand)

    dealerhand = BlackjackHand()
    dealerhand.getCards(deck, 3)
    print(dealerhand)

    
    #Testing Handvalue    
    total = playerhand.handValue()
    print(total)

    tot2 = dealerhand.handValue()
    print(tot2)

    #Testing revealFirstCard
    reveal1 = playerhand.revealFirstCard()
    print(reveal1)

    rev2 = dealerhand.revealFirstCard()
    print(rev2)

    #Testing isBust
    playerbust = playerhand.isBust()
    print(playerbust)

    dealerbust = dealerhand.isBust()
    print(dealerbust)

    #Testing clear
    playercler = playerhand.clear()
    print(playercler)

    dealercler = dealerhand.clear()
    print(dealercler)

if __name__ == "__main__":
    test_BlackjackHand()

