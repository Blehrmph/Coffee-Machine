MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(resources,MENU, decision,end):
    if resources['water']-(MENU[decision]['ingredients']['water'])>0 and resources['milk'] - (MENU[decision]['ingredients']['milk']) > 0 and resources['coffee'] - (MENU[decision]['ingredients']['coffee']) > 0:
        reply=True
        end=""
    else:
        reply=False
        print("Sorry, not enough resources.")
        end="off"
    return reply,end


def report(resources,money):
    print(f"Water: {resources['water']}ml.\nMilk: {resources['milk']}ml.\nCoffee: {resources['coffee']}ml.\nMoney: ${money}.")

def espresso(resources,MENU, money):
    coins=float(input("Please insert money:"))
    if coins > float(MENU['espresso']['cost']):
        money += coins
        change= coins- MENU['espresso']['cost']
        print(f"Here's your change: ${change}.")
        resources['water'] -= (MENU[decision]['ingredients']['water'])
        resources['milk'] -= (MENU[decision]['ingredients']['milk'])
        resources['coffee'] -= (MENU[decision]['ingredients']['coffee'])
        print("Here is your espresso. Enjoy!")
    elif coins < MENU['espresso']['cost']:
        missing= MENU['espresso']['cost'] - coins
        print(f"Sorry, that's not enough money. Money refunded")

def latte(resources,MENU, money):
    coins=float(input("Please insert money:"))
    if coins > float(MENU['latte']['cost']):
        money += coins
        change= coins- MENU['latte']['cost']
        print(f"Here's your change: ${change}.")
        resources['water'] -= (MENU[decision]['ingredients']['water'])
        resources['milk'] -= (MENU[decision]['ingredients']['milk'])
        resources['coffee'] -= (MENU[decision]['ingredients']['coffee'])
        print("Here is your latte. Enjoy!")
    elif coins < MENU['latte']['cost']:
        missing = MENU['latte']['cost'] - coins
        print(f"Sorry, that's not enough money. Money refunded")

def cappuccino(resources,MENU, money):
    coins=float(input("Please insert money:"))
    if coins > float(MENU['cappuccino']['cost']):
        money += coins
        change= coins- MENU['cappuccino']['cost']
        print(f"Here's your change: ${change}.")
        resources['water'] -= (MENU[decision]['ingredients']['water'])
        resources['milk'] -= (MENU[decision]['ingredients']['milk'])
        resources['coffee'] -= (MENU[decision]['ingredients']['coffee'])
        print("Here is your cappuccino. Enjoy!")
    elif coins < MENU['cappuccino']['cost']:
        missing = MENU['cappuccino']['cost'] - coins
        print(f"Sorry, that's not enough money. Money refunded")


end=""
money=0

while end!="off":
    decision=input("What would you like. (espresso/latte/cappuccino):")

    if decision=='espresso':
        reply,end=check_resources(resources,MENU,decision,end)
        if reply==True:
            espresso(resources, MENU, money)

    elif decision=='latte':
        reply,end= check_resources(resources, MENU, decision,end)
        if reply == True:
            latte(resources, MENU, money)

    elif decision=='cappuccino':
        reply,end = check_resources(resources, MENU, decision,end)
        if reply == True:
            cappuccino(resources, MENU, money)

    elif decision=='report':
        print("Report")
        report(resources,money)

    elif decision=='off':
        print("Machine off.")
        end="off"

    else:
        print("Invalid option. Please try again.\n")

