from cardmodels.decks import Deck

def play():  # Это другой комментарий
  # Это еще один комментарий
  score = 0
  d = Deck()
  d.shuffle()

  while True:
    turn = input("Взять карту? ")
    if turn == 'д':
      try:
          current_card = d.deal()
          print(current_card)
      except ValueError as e:
          print(e)
          break
      else:    
          score += len(current_card)
      if score == 21:
        print("Поздравляем!")
        break
      elif score > 21:
        print(f"У вас очков: {score}. Проигрыш! 🙁")
        break
      else:
        print(f"У вас очков: {score}")
    elif turn == 'н':
      print(f"У вас очков: {score}. До свидания!")
      break


if __name__ == "__main__":
  play()
