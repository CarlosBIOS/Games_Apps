import os


def is_word(texto: str) -> str:
    while True:
        if texto.isalpha():
            return texto
        texto: str = input('Please write a word or a sentece: ').casefold().strip()


def yes_or_no(resposta: str) -> str:
    """Gets a `yes` or `no` answer from the user in a case-insensitive loop."""
    while True:
        if resposta in ('yes', 'no'):
            return resposta
        resposta: str = input("Please write 'yes' or 'no': ").casefold().strip()


def is_number(number: str) -> float:
    while True:
        try:
            if isinstance(float(number), float) and float(number) >= 0:
                return float(number)

        except ValueError:
            number: str = input('Please choose a correct number: ')


def main():
    martelo: str = '''
                             ___________
                             \\         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''

    new_dict = {}
    answer = ''

    while answer != 'no':
        print(martelo, '\n')
        name: str = is_word(input('Please write your name: ').casefold().strip())
        bid: float = is_number(input("What is your bid?: "))
        new_dict[name] = bid
        answer: str = yes_or_no(input("Are there any other bidders? Type 'yes or 'no': ").casefold().strip())
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')

    else:
        while answer != 'exit':
            print(f'The winner is {max(new_dict, key=new_dict.get)} with a bid of ${new_dict.get(
                max(new_dict, key=new_dict.get))}')
            answer: str = input('Write exit to close the window.').casefold().strip()


if __name__ == '__main__':
    main()
