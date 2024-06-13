# Criar um jogo:
# 1.º Abrir o cmd e escrever: pip install pyinstaller and pip install cx_Freeze
# 2.º Mudar o dicectory: cd C:\Users\cmmon\Desktop\Estudar\Python\Mega Course\Application 1
# 3.º pyinstaller --onefile jogo_da_forca_function.py
# E abrir a pasta dist
import random
from hangman_words import word_list


def update_code(guess1: str, chosen_word2: str) -> str:
    global lifes
    prototico_word = chosen_word2

    for index, letter in enumerate(chosen_word):
        if guess1 == letter:
            chosen_word2: str = chosen_word2[:index] + guess1 + chosen_word2[index + 1:]

    if prototico_word == chosen_word2:
        lifes -= 1
        print(f'\nResta-te {lifes} lifes')

    return chosen_word2


word: list = word_list
stages = [
    f"""
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
      |
    =========
    """,
    f"""
    +---+
    |   |
    O   |
   /|\\  |
   /    |
      |
    =========
    """,
    f"""
    +---+
    |   |
    O   |
   /|\\  |
      |
      |
    =========
    """,
    f"""
    +---+
    |   |
    O   |
   /|   |
      |
      |
    ========='""",
    f"""
    +---+
    |   |
    O   |
    |   |
      |
      |
    =========
    """,
    f"""
    +---+
    |   |
    O   |
      |
      |
      |
    =========
    """,
    f"""
    +---+
    |   |
      |
      |
      |
      |
    =========
    """,
]
lifes: int = len(stages) - 1

chosen_word: str = random.choice(word)
chosen_word_ = len(chosen_word) * '_'

if __name__ == '__main__':

    logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/    """

    print(logo, '\n')

    while not chosen_word_ == chosen_word:

        print(chosen_word_)
        guess: str = input('Guess a letter: ').casefold().strip()

        chosen_word_ = update_code(guess, chosen_word_)
        print(stages[lifes])

        if lifes == 0:
            print(f'\nThe word is {chosen_word}.\nYou lose and he dies!')
            break

    else:
        print(f'\nYou won, the word is {chosen_word}')
