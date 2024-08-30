import random
from termcolor import colored  
import nltk
from nltk.corpus import words

nltk.download('words')

def get_random_word(word_list):
    return random.choice(word_list).lower()

def get_valid_guess(word_list):
    print("Enter your guess: ")
    while True:
        guess = input().lower()
        if len(guess) == 5 and guess in word_list:
            return guess
        else:
            print(colored("Invalid word. Please enter a valid 5-letter word.", 'red'))

def check_answer():
    word_list = [word.lower() for word in words.words() if len(word) == 5]
    word = get_random_word(word_list)
    
    for attempt in range(1, 7):
        guess = get_valid_guess(word_list)

        for i in range(5):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        
        print()  # Print newline after each attempt

        if guess == word:
            print(colored(f"Congratulations! You got the word in {attempt} guess(es)!", 'green'))
            break
    else:
        print(colored(f"Sorry! The word was {word}. Better luck next time!", 'red'))

check_answer()
