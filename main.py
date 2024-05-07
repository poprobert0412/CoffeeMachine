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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
total_profit = 0

def money():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

def profit(cost):
    global total_profit
    total_profit += cost

def coffee_machine():
    while True:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_choice == "off":
            print("The Coffee Machine is OFF.")
            break
        elif user_choice == "report":
            print(f"Water: {resources['water']}")
            print(f"Milk: {resources['milk']}")
            print(f"Coffee: {resources['coffee']}")
            break
        elif user_choice in MENU:
            select_drink = MENU[user_choice]
            cost_selected_drink = select_drink['cost']
            ingredients_for_drink = select_drink['ingredients']

            can_make = True
            for ingredient, amount in ingredients_for_drink.items():
                if resources[ingredient] < amount:
                    print(f"Sorry, there is not enough {ingredient}.")
                    can_make = False
                    break

            if can_make:
                print("Please insert coins.")
                total_money = money()
                if total_money >= cost_selected_drink:
                    resources['water'] -= ingredients_for_drink.get("water", 0)
                    resources['milk'] -= ingredients_for_drink.get("milk", 0)
                    resources['coffee'] -= ingredients_for_drink.get("coffee", 0)
                    change = total_money - cost_selected_drink
                    print(f"Here is your {user_choice}. Enjoy it!")
                    if change > 0:
                        print(f"Here is your change: ${change:.2f}")
                    profit(cost_selected_drink)
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid input. Please try again")

coffee_machine()
print(f"Total profit earned: ${total_profit:.2f}")