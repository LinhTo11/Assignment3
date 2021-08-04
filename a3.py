import random
import numpy as np

class dice():
  MAX_DICE = 6
  MIN_DICE = 1
  def roll(self):
    return random.randint(dice.MIN_DICE, dice.MAX_DICE)

class dice_game():
  """A game of dice"""
  players = int()
  MINIMUM_CREDIT = 0
  MAXIMUM_ROUND = 25
  DEFAULT_CREDIT = 10
  DEFAULT_ROUND = 0
  dice = dice()

  
  def __init__(self, players = 50, games_played = [], wallet = []):
    self.games_played = games_played     #The number of plays, maximum entry = 25
    self.wallet = wallet    #Each entry in wallet is the player's final credits, minimum = 0
    if players > 0:  
      self.players = players
    else:
      print("beep")
    

  def play(self):
    #initiating the game
    self.round = 0 #This is round 1, or play number 1
    self.credit = self.DEFAULT_CREDIT

    while self.credit > self.MINIMUM_CREDIT and self.round < self.MAXIMUM_ROUND:
      #Let's play again, lose 1 credit, get 1 round
      self.credit -= 1
      self.round += 1
      
      self.grand_total = self.dice.roll() + self.dice.roll()
      if self.grand_total <= 9:
        third_dice = self.dice.roll()
        self.grand_total += third_dice
      elif self.grand_total == 10:
        self.decision = random.randint(0,100)   #Model player's decision with 90% yes
        if self.decision <= 90:                 #If decision is yes
          third_dice = self.dice.roll()
          self.grand_total += third_dice

      if self.grand_total == 10 or self.grand_total == 12:
        self.credit += 1
      elif self.grand_total == 13:
        self.credit += 2
      elif self.grand_total == 16:
        self.credit += 5

  
    self.wallet.append(self.credit) #wallet is a list containing last total credit of a player
    self.games_played.append(self.round)   #games played will contain total plays of a player
    

  def simulate(self):
    for i in range(self.players):
      self.play()


  def avg_rounds(self):
    if self.players > 0:
      result = np.sum(self.games_played) // self.players
      print("Average round is", result)
      return result


  def profit(self): #Net number of credits Casino can make or lose
    casino_net_credit = self.players * self.DEFAULT_CREDIT - sum(self.wallet)
    print("Casino's net credit is", casino_net_credit)
    return  casino_net_credit
      


# day1 = dice_game()
# day1.simulate()
# day1.avg_rounds()
# day1.profit()

# day2 = dice_game(1000)
# day2.simulate()
# day2.avg_rounds()
# day2.profit()

day2 = dice_game()
day2.simulate()
day2.avg_rounds()
day2.profit()


# print(self.wallet)
# print(self.games_played)
# print(len(self.wallet))
# print(len(self.games_played)) 


        


