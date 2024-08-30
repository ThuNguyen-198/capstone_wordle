import nltk
from nltk.corpus import words

nltk.download('words')

words_dictionary = [word for word in words.words() if len(word) == 5]
suggest_word_list = words_dictionary.copy()

while True:
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
        position = input(f"Enter the position of the letter '{letter}' (1-5): ")
        while position not in ['1', '2', '3', '4', '5']:
            position = input(f"Invalid position. Enter a value between 1 and 5 for the letter '{letter}': ")
        position = int(position) - 1

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
