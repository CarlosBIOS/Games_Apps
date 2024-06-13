import os


def yes_or_no(resposta: str) -> str:
    """Gets a `yes` or `no` answer from the user in a case-insensitive loop."""
    while True:
        if resposta in ('yes', 'no'):
            return resposta
        resposta: str = input("Please write 'yes' or 'no': ").casefold().strip()


def is_float(number: str) -> str:
    while True:
        if number == 'exit':
            return number

        try:
            if isinstance(float(number), float):
                return number

        except ValueError:
            number: str = input('Please choose a correct number or exit: ')


def is_sinal(operacao: str) -> str:
    while True:
        if operacao in ('+', '-', '*', '/'):
            return operacao
        operacao: str = input('Please choose an correct operation: ').strip()


def main() -> None:
    """The main function that runs the calculator."""
    logo = """
     _____________________
    |  _________________  |
    | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
    | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
    |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
    | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
    | |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
    | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\  | || |    | |   _   | || |  | |         | |
    | |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
    | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
    | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
    | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
    | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
    |_____________________|
    """

    while True:
        print(logo)
        first_number: str = is_float(input("\nWhat's the first number?: ").strip())

        if first_number == 'exit':
            print('Goodbye!')
            break

        answer = ''
        while answer != 'no':
            for sinal in '+-*/':
                print(sinal)

            operation: str = is_sinal(input('Pick an operation: ').strip())
            second_number: str = is_float(input("What's the next number?: ").strip())
            result: int | float = eval(first_number + operation + second_number)
            print(f'{first_number} {operation} {second_number} = {result}\n')
            first_number = str(result)

            answer: str = yes_or_no(input(f"Type 'yes' to continue calculating with {result}, or type 'no' to start a "
                                          f"new calculation: ").casefold().strip())

        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')


if __name__ == '__main__':
    main()
