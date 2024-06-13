import os
import random
import time
from data_higher_lower import *


def check_a_b(word: str) -> str:
    if word in ('a', 'b'):
        return word
    word: str = check_a_b(input('Please write A or B: ').casefold().strip())


def discover_options() -> dict:
    second_option: dict = random.choice(data)
    del data[data.index(second_option)]
    second_option_values: list = [value for value in second_option.values() if isinstance(value, str)]
    print(f'Compare B: {second_option_values[0]}, a {second_option_values[1]}, from {second_option_values[2]}.')
    return second_option


def play(score: int, first_option: dict, second_option: dict, first):
    answer_user: str = check_a_b(input("Who has more followers? Type 'A' or 'B': ").casefold().strip())
    if answer_user == 'a' and first_option['follower_count'] > second_option['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
        return first_option, score, first
    elif answer_user == 'b' and first_option['follower_count'] < second_option['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}.")
        first = [value for value in second_option.values() if isinstance(value, str)]
        return second_option, score, first

    return {}, score, []


def main():
    score = 0
    first_option: dict = random.choice(data)
    del data[data.index(first_option)]
    first_option_values: list = [value for value in first_option.values() if isinstance(value, str)]
    while first_option != {}:
        print(logo)
        print(f'Your Current Score: {score}')
        print(f"Compare A: {first_option_values[0]}, a {first_option_values[1]}, from {first_option_values[2]}.")
        print(vs)
        second_option = discover_options()
        first_option, score, first_option_values = play(score, first_option, second_option, first_option_values)
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

    else:
        print(f"Sorry, that's wrong. Final score: {score}")


if __name__ == '__main__':
    main()
    time.sleep(15)
