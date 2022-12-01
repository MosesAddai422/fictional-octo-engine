
# Author: <Moses Addai>


from cards import *

from random import randrange

import random

#Allows the user to continue playing the game as long as they have more than $10
def playmanygames():
    money =100
    playerWantsToQuit =  False

    while money>=10 and playerWantsToQuit == False:
        money, playerWantsToQuit = playonegame(money)
        

    print("Goodbye!")
        
#Runs through the game while observing all rules    
def playonegame(money):

    """Plays one game of blackjack.Returns money and true if the player wants to quit and money and False if player wants to play."""
    print()
    print("Welcome to the BlackJack Game!")
    print()
    print("Blackjack Rules")
    print("Kings, Queens, Jacks and Tens are worth 10 points.Aces are worth 1 or 11 (whichever is better for you).")
    print("Cards 2 through 9 are worth their face value.")
    print("\n'Hit' to take another card.")
    print("'Stay' to stop taking cards."\
          "The dealer stops Hitting at 17.")
    print("You start with $100.  Minimum bet is $10.")
    print()

    self = ""

    #n = 2
    
    
    deck = Deck()

    deck.shuffle()

    playerhand = BlackjackHand()
    dealerhand = BlackjackHand()
    

    
    

    
    while money >=10:
        dealerhand.getCards(deck, 2)
        playerhand.getCards(deck, 2)

        dealrev1 = dealerhand.revealFirstCard()
        
        print('\n')
        print("dealer's top card",dealrev1)
    
        print("Your hand",playerhand)
        
        print('\n')
        print("You have",money,"dollars")
        response = input("place minimum bet of $10, or hit <Enter> to Quit ")

        #checks that money entered is appropriate(integer,within available limits)
        while True:
            if response == "":
                return money, True
            try:
                response = int(response)
                if response <10:
                    print("Please enter a value greater than $10")
                    response = input("place minimum bet of $10, or hit <Enter> to Quit ")
                elif response > money:
                    print("You don't have enough money")
                    response = input("place minimum bet of $10 but should not be higher than money, or hit <Enter> to Quit ")
                break
            except:
                print("Not a valid integer")
                response = input("place minimum bet of $10, or hit <Enter> to Quit ")




         #Checking if a natural blackjack has been obtained
        if dealerhand.handValue() == 21:
            print("Dealer got a natural 21. You lose your bet")
            #print("You have ${}".format(money))
            money = money - int(response)
            print("~"*32)
            
        elif playerhand.handValue() == 21:
            print("You got a natural 21. You won your bet")
            money = money + int(response)
            print("~"*32)
           
        elif dealerhand.handValue() == 21 and playerhand.handValue() == 21:
            print("It's a tie. No score lost on both sides")
            print("Dealer's hand:",dealerhand)
            print("Your hand:",playerhand) 
        
        



        
        print("~"*32)

        if response == "":
            print("You have",money,"dollars.Your hand value",playerhand.handValue()," Goodbye!")
            break
        elif response != "":


            #Asks the user for opportunity to double bet if user has enough money and wants to double bet
            
            if (2*int(response)) <= (money-10):
                duobet = input("Do you want to double your bet?(Y/N) ")
                if duobet == "Y":
                    print("Your new best bet is",2*int(response))
                    print("Your hand:",playerhand)

                    
                    hitstay = input("Hit or Stay?(H/S) ")
                    
                    #player wants to stay  
                    if hitstay == "S":
                        print("Dealer's hand:",dealerhand)


                        if dealerhand.isBust() == True:
                            money = money + 2*int(response)
                            print("Dealer went bust!You won", 2*int(response),"and you now have $", money,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                            dealerhand.clear()
                            playerhand.clear()
                            
                            
                        elif playerhand.isBust() == True:
                            money = money - 2*int(response)
                            print("You went bust!You lost", 2*int(response),"and you now have $", money,"Your hand value:",playerhand.handValue())
                            dealerhand.clear()
                            playerhand.clear()
                            
                        elif playerhand.isBust() != True:
                            while dealerhand.handValue() <= 17:
                                dealerhand.getCards(deck, 1)
                                if dealerhand.isBust() == True:
                                    money = money + 2*int(response)
                                    print("Dealer went bust!You won", 2*int(response),"and you now have $", money,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    dealerhand.clear()
                                    playerhand.clear()
                                    break
                                    
                            #neither player nor dealer went bust
                            if playerhand.isBust() != True and dealerhand.isBust() != True:
                                playdiff = 21 - playerhand.handValue()
                                dealdiff = 21 - dealerhand.handValue()

                                if min(playdiff,dealdiff) == playdiff:
                                    money = money + 2*int(response)
                                    print("You won the round! And you now have", money,"dollars left..","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                
                                    dealerhand.clear()
                                    playerhand.clear()
                              
                                
                                if min(playdiff,dealdiff) == dealdiff:
                                    money = money - 2*int(response)
                                    print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                
                                    dealerhand.clear()
                                    playerhand.clear()
                                
                                
                                    

                    #Situation in which player doesn't want to stay
                    else:
                        print("Your hand:",playerhand)
                        playerhand.getCards(deck, 1)
                        print("Your hand:",playerhand)


                            
                    
                        if dealerhand.isBust() == True:
                            money = money + 2*int(response)
                            print("Dealer went bust!You won", 2*int(response),"and you now have $", money,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                            dealerhand.clear()
                            playerhand.clear()
                            
                        elif playerhand.isBust() == True:
                            money = money - 2*int(response)
                            print("You went bust!You lost", 2*int(response),"and you now have $", money ,"Your hand value:",playerhand.handValue())
                            dealerhand.clear()
                            playerhand.clear()
                            
                        elif playerhand.isBust() != True:
                            while dealerhand.handValue() <= 17:
                                dealerhand.getCards(deck, 1)
                                if dealerhand.isBust() == True:
                                    money = money + 2*int(response)
                                    print("Dealer went bust!You won", 2*int(response),"and you now have $", money,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    dealerhand.clear()
                                    playerhand.clear()
                                    break
                                    
                            #if neither player nor dealer goes bust
                            if playerhand.isBust() != True and dealerhand.isBust() != True:
                                playdiff = 21 - playerhand.handValue()
                                dealdiff = 21 - dealerhand.handValue()

                                if min(playdiff,dealdiff) == playdiff:
                                    money = money + 2*int(response)
                                    print("You won the round! And you now have", money,"dollars left.","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    
                                    dealerhand.clear()
                                    playerhand.clear()
##              
                                if min(playdiff,dealdiff) == dealdiff:
                                    money = money - 2*int(response)
                                    print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                    
                                    dealerhand.clear()
                                    playerhand.clear()
##                                
                             


                #Case when player doesn't want to double bet
                else:
                    print("Your hand:",playerhand)
                    hitstay = input("Hit or Stay?(H/S) ")

                    #if player stays
                    if hitstay == "S":
                        print("Dealer's hand:",dealerhand)
##                        dealerhand.getCards(deck, 1)
##                        print("Dealer's hand:",dealerhand)

                        if dealerhand.isBust() == True:
                            money = money + int(response)
                            print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                            dealerhand.clear()
                            playerhand.clear()
                         
                        elif playerhand.isBust() == True:
                            money = money - int(response)
                            print("You went bust!You lost", int(response),"and you now have $", money ,"Your hand value:",playerhand.handValue())
                            dealerhand.clear()
                            playerhand.clear()
                            
                        elif playerhand.isBust() != True:
                            while dealerhand.handValue() <= 17:
                                dealerhand.getCards(deck, 1)
                                if dealerhand.isBust() == True:
                                    money = money + int(response)
                                    print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    dealerhand.clear()
                                    playerhand.clear()
                                    break
                                   

                        #if neither player nor dealer goes bust
                            if playerhand.isBust() != True and dealerhand.isBust() != True:
                                playdiff = 21 - playerhand.handValue()
                                dealdiff = 21 - dealerhand.handValue()

                                if min(playdiff,dealdiff) == playdiff:
                                    money = money + int(response)
                                    print("You won the round! And you now have", money,"dollars left.","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    
                                    dealerhand.clear()
                                    playerhand.clear()
                                
                                if min(playdiff,dealdiff) == dealdiff:
                                    money = money - int(response)
                                    print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                    
                                    dealerhand.clear()
                                    playerhand.clear()
                                
                                    

                    #if player hits
                    else:
                        print("Your hand:",playerhand)
                        playerhand.getCards(deck, 1)
                        print("Your hand:",playerhand)

                            
##            
                            
                    
                        if dealerhand.isBust() == True:
                            money = money + int(response)
                            print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                            dealerhand.clear()
                            playerhand.clear()
                            
                        elif playerhand.isBust() == True:
                            money = money - int(response)
                            print("You went bust!You lost", int(response),"and you now have $", money ,"Your hand value:",playerhand.handValue())
                            dealerhand.clear()
                            playerhand.clear()
                            
                            
                            
                        elif playerhand.isBust() != True:
                            while dealerhand.handValue() <= 17:
                                dealerhand.getCards(deck, 1)
                                if dealerhand.isBust() == True:
                                    money = money + int(response)
                                    print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                    dealerhand.clear()
                                    playerhand.clear()
                                    break
                                    

                        #if neither player nor dealer goes bust
                            
                            if playerhand.isBust() != True and dealerhand.isBust() != True:
                                playdiff = 21 - playerhand.handValue()
                                dealdiff = 21 - dealerhand.handValue()

                                if min(playdiff,dealdiff) == playdiff:
                                    money = money + int(response)
                                    print("You won the round! And you now have", money,"dollars left.","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                            
                                    dealerhand.clear()
                                    playerhand.clear()
                                
                                if min(playdiff,dealdiff) == dealdiff:
                                    money = money - int(response)
                                    print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                    
                                    dealerhand.clear()
                                    playerhand.clear()
                                
                                    


            #Situation in which user does not have enough to double bet
            else:
                print("Your hand:",playerhand)
                hitstay = input("Hit or Stay?(H/S) ")
                #user stays    
                if hitstay == "S":
                    print("Dealer's hand:",dealerhand)
##                    dealerhand.getCards(deck, 1)
##                    print("Dealer's hand:",dealerhand)

                    if dealerhand.isBust() == True:
                        money = money + int(response)
                        print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                        dealerhand.clear()
                        playerhand.clear()
                     
                    elif playerhand.isBust() == True:
                        money = money - int(response)
                        print("You went bust!You lost", int(response),"and you now have $", money ,"Your hand value:",playerhand.handValue())
                        dealerhand.clear()
                        playerhand.clear()
                        
                    elif playerhand.isBust() != True:
                        while dealerhand.handValue() <= 17:
                            dealerhand.getCards(deck, 1)
                            if dealerhand.isBust() == True:
                                money = money + int(response)
                                print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                dealerhand.clear()
                                playerhand.clear()
                                break
                                

                        if playerhand.isBust() != True and dealerhand.isBust() != True:
                            playdiff = 21 - playerhand.handValue()
                            dealdiff = 21 - dealerhand.handValue()

                            if min(playdiff,dealdiff) == playdiff:
                                money = money + int(response)
                                print("You won the round! And you now have", money,"dollars left.","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                dealerhand.clear()
                                playerhand.clear()
                                
                          
                            if min(playdiff,dealdiff) == dealdiff:
                                money = money - int(response)
                                print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                dealerhand.clear()
                                playerhand.clear()
                                
                            
                                    

                #user hits
                else:
                    print("Your hand:",playerhand)
                    playerhand.getCards(deck, 1)
                    print("Your hand:",playerhand)

                            
##                 
                            
                    
                    if dealerhand.isBust() == True:
                        money = money + int(response)
                        print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                        dealerhand.clear()
                        playerhand.clear()
                       
                    elif playerhand.isBust() == True:
                        money = money - int(response)
                        print("You went bust!You lost", int(response),"and you now have $", money ,"Your hand value:",playerhand.handValue())
                        dealerhand.clear()
                        playerhand.clear()
                       
                    elif playerhand.isBust() != True:
                        while dealerhand.handValue() <= 17:
                            dealerhand.getCards(deck, 1)
                            if dealerhand.isBust() == True:
                                money = money + int(response)
                                print("Dealer went bust!You won", int(response),"and you now have $", money ,"Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                dealerhand.clear()
                                playerhand.clear()
                                break
                                

                    #if neither player nor dealer goes bust
                        if playerhand.isBust() != True and dealerhand.isBust() != True:
                            playdiff = 21 - playerhand.handValue()
                            dealdiff = 21 - dealerhand.handValue()

                            if min(playdiff,dealdiff) == playdiff:
                                money = money + int(response)
                                print("You won the round! And you now have", money,"dollars left.","Dealer's hand value is:",dealerhand.handValue(),"Dealer's hand:",dealerhand)
                                dealerhand.clear()
                                playerhand.clear()
                           
                                
                            if min(playdiff,dealdiff) == dealdiff:
                                money = money - int(response)
                                print("The dealer won! You now have",money,"dollars left.","Your hand value:",playerhand.handValue())
                                dealerhand.clear()
                                playerhand.clear()
                                
                           
                                    

                        

                
#player does not have enough money
    else:
        print("You are out of money!Come again next time.")
        return money, True
        


    


def main():
    playmanygames()






if __name__ == "__main__":
    main()      

        

    
