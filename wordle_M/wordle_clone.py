import random
import sys
from termcolor import colored  
import os

file = open("words.txt", "r")
word_list = [i.strip("\n").lower() for i in file]

def get_random_word():
    return random.choice(word_list)

def get_valid_guess(word_list):
    print("Enter your guess: ")
    while True:
        guess = input().lower()
        if len(guess) == 5 and guess in word_list:
            return guess
        else:
            print(colored("Invalid word. Please enter a valid 5-letter word.", 'red'))

def check_answer():
    word = get_random_word()
    for attempt in range(1, 7):
        guess = get_valid_guess(word_list)

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        
        print()  

        if guess == word:
            print(colored(f"Congratulations! You got the word in {attempt} guess(es)!", 'red'))
            break
    else:
        print(colored(f"Sorry! The word was {word}. Better luck next time!", 'red'))