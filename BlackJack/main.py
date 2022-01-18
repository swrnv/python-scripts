from art import logo
import random

def play_game():
  print(logo)
  user_card =[]
  comp_cards = []
  is_game_over = False

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards)==2:
      return 0
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)

  def compare(user_score, comp_score):
    if user_score == comp_score:
      return "Draw 🙃"
    elif comp_score == 0:
      return "The computer won 💻. Computer has a blackJack"
    elif user_score == 0:
      return "You won. You have a blackJack"
    elif user_score > 21:
      return "Computer Wins. You went over 21 "
    elif comp_score >21:
      return "You Win. Computer went over 21"
    elif user_score > comp_score:
      return "You Win. You have a greater score."
    else:
      return f"You loose, Your score :{user_score}, Computer Score : {comp_score}"
    

  def deal_card():
    chosen_card = random.choice(cards)
    return chosen_card

  for _ in range(2):
    user_card.append(deal_card())
    comp_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_card)
    comp_score = calculate_score(comp_cards)
    print(f'Your cards : {user_card}. Current Score : {user_score}')
    print(f"Computer's first card is {comp_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("\n\n Press 'Y' to get another card or 'N' to pass ->  ")
      if user_should_deal == 'Y' or user_should_deal == 'y':
        user_card.append(deal_card())
      else:
        is_game_over = True

  while comp_score!=0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

  print(f"Your Final Hand {user_card}, Final Score : {user_score}")
  print(f"Computer Final Hand {comp_cards}, Final Score : {comp_score}")
  print(compare(user_score, comp_score))



while(input("Do you want to play another round of BlackJacks. Type 'Y' or  'N' ->")) == 'Y':
  play_game()