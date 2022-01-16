import random
from hangman_art import stages, logo
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(logo) 
print(chosen_word)
display = []
already_guessed =[]
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in already_guessed:
      print(f'You have already guessed the letter {guess}, keep trying')
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            already_guessed.append(guess)
    if guess not in already_guessed:
      if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'{guess} is not a letter, You lose a life') 
        already_guessed.append(guess) 
        if lives == 0:
            end_of_game = True
            print(f"\n\n|=| You lose. The word was {chosen_word} |=|\n\n")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("\n\n |=| You win !!! You guessed correctly. |=|\n\n")