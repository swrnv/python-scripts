from art import logo
from random import randint

def check_answer(guess, num):
  if guess > num:
    print('Too High')
  elif guess < num:
    print('Too Low')
  elif guess == num:
    print(f'Kudos !! You guessed it correctly. The actual answer was {num}.')

print(logo)
print('Welcome to the guessing game !!!')
print('I am thinking a number between 1 and 100')
num = randint(1,100)
level = input("Type 'Easy' or 'Hard' for level difficulty : ")
if level == 'Easy' :
  lives = 12 
  print('You have 12 lives to guess the number')
elif level == 'Hard':
  lives = 6
  print('You have 6 lives to guess the number')

while lives !=0:
  guess = int(input('\n Guess the Number -> '))
  print(f'You have {lives} remaining.')
  check_answer(guess, num)
  lives -= 1


