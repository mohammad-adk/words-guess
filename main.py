import glob
import os
import random
from my_utils import *

# change directory to the files directory
os.chdir("c:\\Users\\moham\\Documents\\python_projects\\word_guess\\files")
words = {}
for file in glob.glob("*.txt"):
    f = open(file, 'r')
    words[file[:-4]] = []
    for word in f:
        words[file[:-4]].append(word)


while True:
    print("""1. predict the word's characters 
    2. predict the whole word
    3. quit
    """)
    category = random.choice(list(words.keys()))  # choose a random category
    # choose a random word from the chosen category
    word_index = random.randint(0, len(words[category]))
    word = words[category][word_index][:-1].lower()
    guessed_word = '_ ' * len(word)
    option = input('Please select : ')
    if option == '1':
        tries = len(word)
        finished = False
        currect_count = 0
        message = ''
        while tries > 0 and not finished:
            print('\033c')  # clear the console
            print(category)
            print(message)
            print(guessed_word)
            char = input('Please input your guess: ').lower()
            if guessed_word.find(char) >= 0:
                message = 'the char is duplicate'
                continue
            char_indices = find_all(char, word)
            if len(char_indices) > 0: # character is correct
                currect_count += len(char_indices)
                if currect_count == len(word):
                    print('\033c')
                    print(f"""Yeeees You won the game. 
                    The word was {word}""")
                    finished = True
                    continue
                else:
                    message = f'it was correct. chances left is {tries}'
                    for char_index in char_indices:
                        guessed_word = guessed_word[:char_index*2] + \
                            char + guessed_word[char_index*2+1:] # add char to guessed word
                
            else: #character is wrong
                tries -= 1
                if tries <= 0:
                    print('\033c')
                    print(f'You lose the word was {word}')
                    break
                message = f'It was incorrect. chances left is {tries}'

    elif option == '2':
        print(2)
    elif option == '3':
        quit()
    else:
        print('Unknown Option Selected!')
