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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ing(make_coffee):
    for key in MENU[make_coffee]["ingredients"]:
        if resources[key] >= MENU[make_coffee]["ingredients"][key]:
            new_water = resources[key] - (MENU[make_coffee]["ingredients"][key])
            resources[key] = new_water

        else:
            print(f"Sorry, there is not enough {key}.")
            order()


def change(make_coffee):
    print("Please insert coins.")
    quarters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))

    sum=(quarters*25)+(dimes*10)+(nickles*5)+pennies
    coffee_cost=(MENU[make_coffee]["cost"])*100

    if sum >= coffee_cost:
        conclusion = (sum-coffee_cost)/100
        print(f"Here is a ${conclusion} in change.")
    else:
        print("Sorry that's not enough money. Money refunded.")
        order()

    print(f"Here is your {make_coffee}. Enjoy!")
    order()


def order():
    make_coffee = input("What would you like? (espresso/latte/cappuccino):").lower()

    if make_coffee in MENU:
        check_ing(make_coffee)
        change(make_coffee)

    elif make_coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        
    elif make_coffee == "off":
        exit()
        
    else:
        print("\nSorry, we do not have that coffee :/")


order()
