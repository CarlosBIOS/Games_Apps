import os
import time


def check_prompt(user_choice: str) -> str:
    while True:
        if user_choice in ('expresso', 'latte', 'cappuccino', 'off', 'resources'):
            return user_choice
        user_choice: str = input('Please choose a correct option: ').casefold().strip()


def check_coins(coins_user: list, user_choice_coffee: float) -> list | float:
    coin_manage: dict = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.1, 'quarter': 0.25}
    result: float = 0.0
    for value in coins_user:
        split_value = [''. join(elem for elem in value if elem.isdigit()), ''. join(elem for elem in value if
                                                                                    elem.isalpha())]

        result += float(split_value[0]) * coin_manage.get(split_value[1])
        print(result)

    if result < user_choice_coffee:
        print(f'Sorry, {result} não é suficiente. É preciso {user_choice_coffee}. Money refunded.')
        return 0
    elif result > user_choice_coffee:
        print(f'Here is ${round(result-user_choice_coffee, 2)} dollars in change.')

    return user_choice_coffee


def main():
    logo = '''
 __   __   __   ___  ___  ___                __               ___ 
/  ` /  \\ /  \\ |__  |__  |__      |\\/|  /\\  /  ` |__| | |\\ | |__  
\\__, \\__/ \\__/ |    |    |___     |  | /~~\\ \\__, |  | | | \\| |___ 
                                                                  
'''
    coffee_list: dict = {
        'expresso': {'Water': 50, 'Coffee': 18, 'price': 1.5},
        'latte': {'Water': 200, 'Coffee': 24, 'Milk': 150, 'price': 2.5},
        'cappuccino': {'Water': 250, 'Coffee': 24, 'Milk': 100, 'price': 3},
    }
    machine_resources: dict = {'Water': 300, 'Coffee': 100, 'Milk': 200, 'Price': 0}
    result = 0
    print(logo)
    while True:
        user_choice: str = check_prompt(input("\nWhat would you like?\nExpresso/Latte/Cappuccino\nWrite off to turn off"
                                              " the machine or report to show the resources\n->").casefold().strip())
        if user_choice == 'off':
            break
        elif user_choice == 'resources':
            for key, value in machine_resources.items():
                print(f'{key}: {value}')
        else:
            user_choice_coffee: dict = coffee_list[user_choice]
            for values in ('Water', 'Coffee', 'Milk'):
                if user_choice_coffee.get(values, 0) > machine_resources.get(values):
                    print(f"Sorry there is not enough {values.casefold()}.")
                    break

            while result == 0:
                coins_user: list = input('Please insert the coins: ').casefold().replace(' ', '').split(',')
                result: float = check_coins(coins_user, user_choice_coffee['price'])

            for value in ('Water', 'Coffee', 'Milk'):
                machine_resources[value] -= user_choice_coffee.get(value, 0)
            machine_resources['Price'] += result

            print(f'Here is your {user_choice}☕. Enjoy!')
            time.sleep(10)

            if os.name == 'nt':
                os.system('cls')
            elif os.name == 'posix':
                os.system('clear')

            print(logo)


if __name__ == '__main__':
    main()
