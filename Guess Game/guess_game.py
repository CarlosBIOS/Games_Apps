import random
import os


def yes_or_no(resposta: str) -> str:
    """Gets a `yes` or `no` answer from the user in a case-insensitive loop."""
    while True:
        if resposta in ('yes', 'no'):
            return resposta
        resposta: str = input("Please write 'yes' or 'no': ").casefold().strip()


def check_difficulty(easy_or_hard: str) -> str:
    """Serve para verificar se o input `easy_or_hard` tem como valor easy ou hard"""
    while True:
        if easy_or_hard in ('easy', 'hard'):
            return easy_or_hard
        easy_or_hard: str = input('Please write easy or hard: ').casefold().strip()


def check_is_number(number: str) -> int:
    """Verifica se `number` is a correct integer"""
    while True:
        try:
            return int(number)

        except ValueError:
            number: str = input('Please write a correct number integer: ').strip()


def begin_information(low_value: int, high_value: int) -> int:
    """Vai print the `logo` and return an integer between 1 and 100."""
    logo: str = '''
   ______                        __  __            _   __                __             
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \\/ ___/ ___/  / __/ __ \\/ _ \\   /  |/ / / / / __ `__ \\/ __ \\/ _ \\/ ___/
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\\____/\\__,_/\\___/____/____/   \\__/_/ /_/\\___/  /_/ |_/\\__,_/_/ /_/ /_/_.___/\\___/_/     
                                                                                        
'''
    print(logo)
    print("Welcome to the Number Guessing Game!", f"I'm thinking of a number between {low_value} and {high_value}.")
    return random.randint(low_value, high_value)


def guess_the_number(solution, attempts: int) -> None:
    while attempts != 0:
        guess: int = check_is_number(input('Make a guess: ').strip())
        if guess < solution:
            print('Too Low')
        elif guess > solution:
            print('Too High')
        else:
            print(f'You got it! The answer was {solution}.')
            break
        attempts -= 1
        print(f"\nYou have {attempts} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses, you lose.", f'The answer was {solution}.')


def play(easy_or_hard: str, solution: int) -> str:
    attempts = 10 if easy_or_hard == 'easy' else 5
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
    guess_the_number(solution, attempts)

    return yes_or_no(input("\nDo you want play again? Write 'yes' or 'no': ").casefold().strip())


def main():
    low_value: int = 1
    high_value: int = 100
    answer = ''
    while answer != 'no':
        solution_value: int = begin_information(low_value, high_value)
        easy_or_hard: str = check_difficulty(input(f"Choose a difficulty. Type 'easy' or 'hard': ").casefold().strip())
        answer: str = play(easy_or_hard, solution_value)
        if os.name == 'nt':  # Check if the OS is windows
            os.system('cls')
        elif os.name == 'posix':  # Check if the OS is Mac/linux
            os.system('clear')


if __name__ == '__main__':
    main()
