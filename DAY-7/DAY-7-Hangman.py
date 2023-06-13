from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

import random
#word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)


guessList = []


display = []
for _ in range(word_length):
    display += "_"


end_of_game = False
lives = 6
while not end_of_game:
    guess = input("Guess a letter: ").lower()

        
        
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            if guess in guessList:
                print(f"You have already guessed {guess}")
            display[position] = letter

    if guess not in chosen_word:
        if guess in guessList:
            print(f"You have already guessed {guess}")
        else:    
            lives = lives - 1
    if lives == 0:
        print(f"You lose. The word was {chosen_word}")
        print(stages[lives])
        break

    guessList += guess
    print(display)
    print(stages[lives])
   # print(guessList)
    
    if "_" not in display:
        end_of_game = True
        print("You win.")