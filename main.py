import glob
import os
import random

os.chdir("c:\\Users\\moham\\Documents\\python_projects\\word_guess\\files") # change directory to the files directory
words = {} 
for file in glob.glob("*.txt"):
    f = open(file, 'r')
    words[file[:-4]] = []
    for word in f:
        words[file[:-4]].append(word)



while True:
    print ("""1. predict the word's characters 
    2. predict the whole word
    3. quit
    """)
    category = random.choice(list(words.keys())) # choose a random category
    word_index = random.randint(0,len(words[category])) # choose a random word from the chosen category
    word = words[category][word_index][:-1] 
    guessed_word = '_ ' * len(word)
    print(word)
    option = input('Please select :')
    if option == '1':
        tries = len(word)
        finished = False
        while tries > 0 and finished:
            print(guessed_word)
            char = input('Please input your guess: ')
            char_index = word.find(char)
            if char_index >= 0 :
                guessed_word[char_index * 2] = char
            else:
                tries -= 1
                
        
    elif option == '2':
        print(2)
    elif option == '3':
        quit()
    else:
        print('Unknown Option Selected!')




