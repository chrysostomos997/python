from data_coffee import MENU, resources

def is_transaction_successful(money,drink_cost):
    if money > drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False






def check_resources(choose):
    ingredients_needed = MENU[choose]['ingredients']
    for item, quantity_needed in ingredients_needed.items():
        if resources[item] < quantity_needed:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def make_the_coffee(choose):
    if check_resources(choose):
        if choose == "espresso":
            resources['water'] -= MENU['espresso']['ingredients']['water']
            resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
            print("Here is your espresso. Enjoy!")
        elif choose == "latte":
            resources['water'] -= MENU['latte']['ingredients']['water']
            resources['coffee'] -= MENU['latte']['ingredients']['coffee']
            resources['milk'] -= MENU['latte']['ingredients']['milk']
            print("Here is your latte. Enjoy!")
        else:
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
            resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
            print("Here is your cappuccino. Enjoy!")

is_running = True
while is_running:
    choose = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    money = float(input ("Please insert some coins: "))
    if choose == "off":
        is_running = False
    elif choose == "report":
        print("Water:", resources['water'])
        print("Milk:", resources['milk'])
        print("Coffee:", resources['coffee'])
    elif choose == "cost":
        print("Espresso: ", MENU['espresso']['cost'])
        print("Latte: ", MENU['latte']['cost'])
        print("Cappuccino: ", MENU['cappuccino']['cost'])
    elif choose in ["espresso", "latte", "cappuccino"] and is_transaction_successful(money,MENU[choose]['cost']):
        make_the_coffee(choose)















#
#
#
#
