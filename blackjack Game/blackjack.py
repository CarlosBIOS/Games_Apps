# Our Blackjack House Rules:

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

# Hint 1: Go to this website and try out the Blackjack game:
# https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
# https://appbrewery.github.io/python-day11-demo/
import random
import os


def yes_or_no(resposta: str) -> str:
    """Gets a `yes` or `no` answer from the user in a case-insensitive loop."""
    while True:
        if resposta in ('yes', 'no'):
            return resposta
        resposta: str = input("Please write 'yes' or 'no': ").casefold().strip()


def deck_user_display(user_deck: list, card: list) -> list:
    """Asks the user to hit or stay, dealing cards until they stay or bust."""
    while sum(user_deck) < 22:
        choice: str = yes_or_no(input("\nType 'yes' to get another card, type 'no' to pass: ").casefold().strip())
        if choice == 'no':
            return user_deck

        user_deck.append(random.choice(card))

        if 11 in user_deck and sum(user_deck) > 21:
            user_deck[user_deck.index(11)] = 1

        print(f"Your cards: {user_deck}, current my_score: {sum(user_deck)}")

    return user_deck


def deck_dealer_display(dealer_deck: list, card: list, deck_user: list) -> list:
    """Deals cards to the dealer until their my_score is at least 17."""
    while sum(dealer_deck) < sum(deck_user):
        dealer_deck.append(random.choice(card))

        if 11 in dealer_deck and sum(dealer_deck) > 21:
            dealer_deck[dealer_deck.index(11)] = 1

    return dealer_deck


def display_information(logo, deck_user, deck_dealer):
    print(logo)
    print(f'Your cards: {deck_user}, current my_score: {sum(deck_user)}')
    print(f"Dealer's first card: {deck_dealer[0]}")


def determine_winner(user_hand, dealer_hand):
    """Compares the user and dealer's scores to determine the winner."""

    user_score = sum(user_hand)
    dealer_score = sum(dealer_hand)

    if dealer_score > 21:
        return "You win! Dealer went over 21."
    elif user_score > dealer_score:
        return "You win!"
    elif user_score < dealer_score:
        return "You lose."
    else:
        return "It's a draw!"


def play(cards: list, logo: str):
    deck_user: list = random.sample(cards, 2)
    deck_dealer: list = [random.choice(cards)]

    display_information(logo, deck_user, deck_dealer)

    deck_user: list = deck_user_display(deck_user, cards)

    print(f"\nYour final hand: {deck_user}, final my_score: {sum(deck_user)}")

    if sum(deck_user) > 21:
        print('You went over. You lose')

    else:
        deck_dealer: list = deck_dealer_display(deck_dealer, cards, deck_user)

        print(f"Dealer's final hand: {deck_dealer}, final my_score: {sum(deck_dealer)}")

        print(determine_winner(deck_user, deck_dealer))


def main():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""
    cards: list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    play_again: str = ''

    while play_again != 'no':
        play(cards, logo)

        play_again: str = yes_or_no(input("\nDo you want to play again? Type 'yes' or 'no': ").casefold().strip())
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')


if __name__ == '__main__':
    main()
