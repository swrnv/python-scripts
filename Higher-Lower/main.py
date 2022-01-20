import random
from art import logo, vs
from game_data import data
from replit import clear

#format the data
def format_data(account):
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]

  return (f'{account_name}, a {account_desc} from {account_country}')

def check_guess(guess, a_followers, b_followers):
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'
  

print(logo)
score = 0
game_continues = True
peep_b = random.choice(data)

while game_continues:
  #find two random people from game data
  peep_a = peep_b
  peep_b = random.choice(data)
  if peep_a == peep_b:
    peep_b = random.choice(data)

  print(f"Compare A : {format_data(peep_a)}")
  print(vs)
  print(f"Agaisnt B : {format_data(peep_b)}")
  guess = input("Who has more instagram followers: Type 'A' or 'B' -> ").lower()

  a_followers = peep_a['follower_count']
  b_followers = peep_b['follower_count']
  #create a score keeper

  clear()
  print(logo)
  is_correct = check_guess(guess, a_followers, b_followers)


  #Giving feedback and keeing track if the score

  if is_correct:
    score +=1
    print(f'You are correct !!. current score : {score}')
  else:
    print(f'Oops!! You are wrong. Final Score : {score}')
    game_continues = False