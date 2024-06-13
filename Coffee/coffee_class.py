from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu_available = Menu()  # latte/espresso/cappuccino/

while is_on:
    user_choice = input(f'Please choose a option {menu_available.get_items()[:-1]}: ').casefold().strip()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu_available.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
