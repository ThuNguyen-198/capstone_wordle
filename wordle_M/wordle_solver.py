import random
import sys
from termcolor import colored
import os

file = open("words.txt", "r")
word_list = [i.strip("\n").lower() for i in file]\

letter = 'a'
position = 0
suggest_word_list = word_list.copy()

while letter != '':
    letter = input("Enter a single letter or press Enter to quit: ").lower()
    if letter == '':
        break

    # Validate letter input
    while len(letter) != 1 or not letter.isalpha():
        letter = input("Invalid input. Please enter a single letter: ").lower()
        if letter == '':
            break

    if letter == '':
        break

    color = input(f"Enter the color of the letter '{letter}' (g/y/b): ").lower()
    while color not in ["g", "y", "b"]:
        color = input("The color can only be 'g', 'y', or 'b': ").lower()


    if color in ['g', 'y']:
        position = input("Enter the position of letter {letter} (1-5): ")
        while position not in ['1','2','3','4','5']:
            position = input(f"Position can only have value 1, 2, 3, 4, or 5.\nEnter the position of the letter '{letter}' (1-5): ")
        position = int(position)-1

    for i in range(len(suggest_word_list) - 1, -1, -1):
        word = suggest_word_list[i]
        
        if color == 'g':
            if word[position].lower() != letter:
                suggest_word_list.pop(i)
        
        elif color == 'y':
            if letter not in word or word[position].lower() == letter:
                suggest_word_list.pop(i)
        
        elif letter in word:
            suggest_word_list.pop(i)

    print(f"Possible words ({len(suggest_word_list)}): ")
    print(suggest_word_list)
