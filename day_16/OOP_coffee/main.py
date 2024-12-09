#from menu import Menu, MenuItem
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# I noticed that in the course solution, one pay and not get coffee


exit=False
menu=Menu()
coffee=CoffeeMaker()
money=MoneyMachine()
print("Welcome to our Coffee Machine!")
while(not exit):
    command=input(f"\nWhat would you like? {menu.get_items()}\n")
    if command== "report":
        coffee.report()
        money.report()
    elif command=="exit": 
        print("\nThank you for using our coffee machine, have a nice day!")
        exit=True
    else:
        drink_found=False
        for item in menu.menu:
            if command==item.name:
                if coffee.is_resource_sufficient(item) and money.make_payment(item.cost):
                    coffee.make_coffee(item)
                drink_found=True
                break
        if not drink_found:
            print("\nDrink not recognized. :(")
        
    anything_else_match=False
    while(not anything_else_match):
        match input("\nAnything else ? (yes/no)\n"):
            case "yes"|"Yes":
                anything_else_match=True
                exit=False
            case "no"|"NO":
                anything_else_match=True
                print("\nThank you for using our coffee machine, have a nice day!")
                exit=True
            case _:
                print("\nCommand not supported, please try again.")