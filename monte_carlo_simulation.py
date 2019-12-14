import random
import matplotlib.pyplot as plt

class Game():
    def __init__(self):
        self.ending_sums = []     # list for final funds 
        
        
    def spinRoulette(self):
        # if pocket is red (even number), the player wins
        # if number is odd, the house wins
        
        pocket = random.randint(1, 37)        
        return True if pocket % 2 == 0 else False



    def play(self, total_funds, amount, number_of_bets):
        
        # function to play the game:
        # total_funds = total money the player is starting with
        # amount = the betting amount each time the player plays
        # numSpins =  the number of times the player bets 
        
    
        funds = []
    
        for spin in range(number_of_bets):
            
            if spinRoulette():  # the player wins                
                total_funds = total_funds + amount            
            
            else:  # the house wins
                total_funds = total_funds - amount
            
            funds.append(total_funds)
            
        plt.plot(range(number_of_bets), funds)  # рисуем 1-я ставка - 9700, 2я ставка -9400..
        self.ending_sums.append(funds[-1])  # add the final balance after <number_of_bets> spinning
     
    def getAverageTotal(self):
        return sum(self.ending_sums)/len(self.ending_sums) 
    

# Simulate the plays and calculate the remaining funds of the player after all the bets
        
START_SUM = 1000
BET = 100
N_OF_BETS = 10

my_game = Game()
for i in range(1000): 
    my_game.play(START_SUM, BET, N_OF_BETS)  # starting sum is 10000$, 1 bet is 100$, 10 times
    
#Plot the line plot of "Account Value" vs "The number of plays"
plt.ylabel('Player\'s money, $')
plt.xlabel('Number of bets')
plt.show()

print("The player starts the game with ${} and ends with ${}".format(START_SUM, my_game.getAverageTotal()))
    