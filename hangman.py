import random
from words import words
import string

def get_valid_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    choices = 0
    user_quit = False

    while len(word_letters) > 0 and choices < 26:
        #getting the user input

        print('You have used these letters ', ' '.join(used_letters),
              'Choices left: '+str(26 - choices))

        print('The word formed until now: ', 
              ' '.join([letter if letter in used_letters else '-' for letter in word]))

        user_letter = input('Guess a letter or (Quit) to quit: ').upper()
        if user_letter == 'QUIT':
            user_quit = True
            break
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        
        elif user_letter in used_letters:
            print("You have already used the character. Please try again")

        else:
            print("Invalid Character. Please Try again")
        
        choices += 1

    if user_quit:
        print('Sorry you don\'t have any score')
    
    print(f'Your Score: {(26 - choices)}')

    print(f'Correct word is {word}')

hangman()

