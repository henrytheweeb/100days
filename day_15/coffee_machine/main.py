MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "ingredients": {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        },
        "profit": 0,
}
def print_report():
    print("\nCURRENT MACHINE STATUS:")
    print("Ingredients:")
    for i_ingredient in resources["ingredients"].keys():
        print("{}: {} remaining".format(i_ingredient,resources["ingredients"][i_ingredient]))
    print("The machine has made {} profit".format(resources["profit"]))

def enough_resources(drink):
    for i_ingredient in MENU[drink]["ingredients"].keys():
        if MENU[drink]["ingredients"][i_ingredient]> resources["ingredients"][i_ingredient]:
            return False
    return True
def get_change(drink,penny,nickel,dime,quarter):
    return penny*0.01+nickel*0.05+dime*0.1+quarter*0.25-MENU[drink]["cost"]
def update_machine(drink):
    for i_ingredient in MENU[drink]["ingredients"].keys():
        resources["ingredients"][i_ingredient]-=MENU[drink]["ingredients"][i_ingredient]
    resources["profit"]+=MENU[drink]["cost"]
    
#MACHINE WORKING LOOP 
    
exit=False
print("Welcome to our Coffee Machine!")
while(not exit):
    command=input("\nWhat would you like? (espresso/latte/cappuccino)\n")
    match command:
        case "report":
            print_report()
        case "exit": 
            print("\nThank you for using our coffee machine, have a nice day!")
            exit=True
        case "espresso"|"latte"|"cappuccino":
            print("\nPlease insert the required funds ({:.2f}):".format(MENU[command]["cost"]))
            n_penny=int(input("Pennies: "))
            n_nickel=int(input("Nickels: "))
            n_dime=int(input("Dimes: "))
            n_quarter=int(input("Quarters: "))
            change=get_change(drink=command,
                              penny=n_penny,
                              nickel=n_nickel,
                              dime=n_dime,
                              quarter=n_quarter)            
            if not enough_resources(command):
                print("Unfortunately, we do not have enough resources to prepare your drink")
            elif change<0:
                print("You lack the required funds for that drink. (missing {:.2f})".format(-1*change))
            else:
                print("Preparing your {}".format(command))
                print("Giving {:.2f} change".format(change))
                update_machine(command)                
        case _:
            print("Command not supported")
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

