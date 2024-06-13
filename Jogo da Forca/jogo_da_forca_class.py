# Criar um jogo:
# 1.º Abrir o cmd e escrever: pip install pyinstaller and pip install cx_Freeze
# 2.º Mudar o dicectory: cd C:\Users\cmmon\Desktop\Estudar\Python\Mega Course\Application 1
# 3.º pyinstaller --onefile jogo_da_forca_function.py
# E abrir a pasta dist
import random
from hangman_words import word_list


class Hangman:

    def __init__(self, words_list):
        self.word = random.choice(words_list)
        self.word_to_guess = len(self.word) * '_'
        self.lifes = len(stages) - 1
        self.stages = stages
        self.logo = logo

    def play(self):
        print(self.logo, '\n')
        while self.word_to_guess != self.word:
            print(self.word_to_guess)
            guess: str = input('Guess a letter: ').casefold().strip()

            self.update_word(guess)
            print(self.stages[self.lifes])

            if self.lifes == 0:
                print(f'\nThe word is {self.word}.\nYou lose and he dies!')
                break

        else:
            print(f'\nYou won, the word is {self.word}')

    def update_word(self, guess):
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            return

        prototico_word = self.word_to_guess
        for index, letter in enumerate(self.word):
            if guess == letter:
                self.word_to_guess = self.word_to_guess[:index] + guess + self.word_to_guess[index + 1:]

        if prototico_word == self.word_to_guess:
            self.lifes -= 1
            print(f'You have {self.lifes} lifes left')


if __name__ == '__main__':
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

    logo = """
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |                      
                       |___/    """
    while True:
        Hangman(word_list).play()
