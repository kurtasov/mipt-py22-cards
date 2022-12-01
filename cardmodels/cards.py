class Card():
  def __init__(self, suit, value):
    self.suit = suit
    self.value = value

  def __repr__(self):
    return f'{self.value} {self.suit}'

  def __len__(self):
    if self.value == 'A':
      return 11
    elif self.value == 'K':
      return 4
    elif self.value == 'Q':
      return 3      
    elif self.value == 'J':
      return 2    
    else:
      return self.value