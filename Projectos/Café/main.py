from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_on = True

while machine_on:
    options = menu.get_items()
    order = input(f"What do you want? {options}")

    if order == "off":
        machine_on = False

    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
           if print(money_machine.make_payment(drink.cost)):
               coffee_maker.make_coffee(drink)
