import random
import numpy as np

class dice():
  MAX_dice = 6
  MIN_dice = 1
  def roll(self):
    return random.randint(dice.MIN_dice, dice.MAX_dice)

class dice_game:
  """A game of dice"""
  players = 50
  wallet = []     #Each entry in wallet is the player's final credits, minimum = 0
  games_played = []     #The number of plays, maximum entry = 25
  MINIMUM_CREDIT = 0
  MAXIMUM_ROUND = 25
  DEFAULT_CREDIT = 10
  DEFAULT_ROUND = 0
  dice = dice()

  
  def __init__(self, players = None):
    if (players != None):
      self.players = players

  def play(self):
    #initiating the game
    self.round = 0 #This is round 1, or play number 1
    self.credit = dice_game.DEFAULT_CREDIT

    while self.credit > dice_game.MINIMUM_CREDIT and self.round < dice_game.MAXIMUM_ROUND:
      #Let's play again, lose 1 credit, get 1 round
      self.credit -= 1
      self.round += 1
      
      self.grand_total = dice_game.dice.roll() + dice_game.dice.roll()
      if self.grand_total <= 9:
        third_dice = dice_game.dice.roll()
        self.grand_total += third_dice
      elif self.grand_total == 10:
        self.decision = random.randint(0,100)   #Model player's decision with 90% yes
        if self.decision <= 90:                 #If decision is yes
          third_dice = dice_game.dice.roll()
          self.grand_total += third_dice

      if self.grand_total == 10 or self.grand_total == 12:
        self.credit += 1
      elif self.grand_total == 13:
        self.credit += 2
      elif self.grand_total == 16:
        self.credit += 5

  
    dice_game.wallet.append(self.credit) #wallet is a list containing last total credit of a player
    dice_game.games_played.append(self.round)   #games played will contain total plays of a player

  def simulate(self):
    for i in range(self.players):
      self.play()


  def avg_rounds(self):
    result = np.sum(dice_game.games_played) // self.players
    print("Average round is", result)
    return result


  def profit(self): #Net number of credits Casino can make or lose
    casino_net_credit = self.players * dice_game.DEFAULT_CREDIT - sum(dice_game.wallet)
    print("Casino's net credit is", casino_net_credit)
    return  casino_net_credit
      


# day1 = dice_game()
# day1.simulate()
# day1.avg_rounds()
# day1.profit()

day2 = dice_game(1000)
day2.simulate()
day2.avg_rounds()
day2.profit()


# print(dice_game.wallet)
# print(dice_game.games_played)
# print(len(dice_game.wallet))
# print(len(dice_game.games_played))


        

