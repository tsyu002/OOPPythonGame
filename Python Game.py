import random, time

#define object: die and roll die
class die(object):
    def roll(self):
        self.value = random.randint(1,6)
        return self.value
    
#define object: card
class card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__( self ):
        return "%2s%s" % (self.rank, self.suit)

#define object: coin and flip coin
class coin(object):
    def __init__(self):
        self.side = 'side'
    def flipping (self):
        flip = random.randint(0,1) #0 for tails and 1 for heads
        if flip == 0:
            self.side = 'Tails'
        else:
            self.side = 'Heads'
    def flip_result (self):
        return self.side

#routine to roll die, draw card, flip coin
def main():
    
    winner = 0 #User will continue to play while winner = 0. winner = 1 when winning condition met
    i = 1 #Initialize row number for file where results will be written
    results = open("game_results.txt", "w+") #create file to write results
    
    #error handling in case user types anything other than yes or no
    while True:
        play = input("Would you like to play? (yes/no):")
        if(play != "yes" and play != "no"):
            print("Invalid entry. Please try again.")
            continue
        else:
            break

    #if enter game routine if user chooses to play
    if (play == "yes"):
        while winner < 1:
            #Roll die
            input("Press the 'Enter' key when you are ready to roll the dice. ")
            d1 = die()
            a = d1.roll()
            time.sleep(1)
            print("You rolled:", a)
            
            #Draw card
            input("Press the 'Enter' key when you are ready to draw a card. ")
            numbers = list(range(2,11)) #Cards 2-10
            numbers.extend(['Jack', 'Queen', 'King', 'Ace']) #Add face cards list
            c = card(random.choice(numbers) , random.choice([' of Hearts', ' of Diamonds', ' of Spades', ' of Clovers'])) #Draw random card
            time.sleep(1)
            print("Your card is:", c)
            
            #Flip Coin
            input("Press the 'Enter' key when you are ready to flip the coin. ")
            cn = coin()
            cn.flipping() #Flip coin
            b = cn.flip_result()
            time.sleep(1)
            print("The coin is:", b)   

            print("You rolled a",a,", drew a",c, ", and flipped",b)

            #Write results to file created earlier
            results = open("game_results.txt", "a+")
            results.write("Attempt %d: You rolled a %d, drew a %s, and flipped a %s\n\r" %(i, a, c, b))
            i = i+1 #Increment i to write next results to next lines
            
            #Set winning conditions. dice roll: 6, coin flip: heads, card drawn: J of Spades or Ace of Diamonds
            if (a == 6 and b == "Heads" and (c == "Jack of Spades" or c == "Ace of Diamonds")):
                winner = 1 #If user wins the condition to exit while loop is met
                print("Congratulations! You win!")
            else:
                time.sleep(1)
                print("You did not get a winning combination. Please try again.")
            
    else:
        print("See you next time!") #If user selects no when asked "Would you like to play?"

#Execute game routine
main()
