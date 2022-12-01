from random import shuffle
from cardmodels.cards import Card

class Deck():

  def __init__(self):
    suits = ['♠️', '♥️', '♦️', '♣️']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    self.cards = [Card(suit, value) for suit in suits for value in values]

  def __repr__(self):
    return str(len(self.cards))
  
  def __len__(self):
    return len(self.cards)

  def deal(self):
    if len(self) > 0:
      return self.cards.pop()
    else:
      raise ValueError('Колода пуста! Невозможно выдать карту!')

  def shuffle(self):
    shuffle(self.cards)