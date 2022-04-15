# Stage 3
"""
Amount of ingredients per coffee

esp_coffee = 16
esp_water = 250
esp_money = 4

latte_coffee = 20
latte_water = 350
latte_milk = 75
latte_money = 7

cap_coffee = 12
cap_water = 200
cap_milk = 100
cap_money = 6
"""

# To make 1 cup of coffee, we need:
WATER = 400
MILK = 540
COFFEE = 120
CUP = 9
MONEY = 550


def show_remaining():
    global WATER, MILK, COFFEE, CUP, MONEY

    print(f"""
        {WATER} ml water
        {MILK} ml milk
        {COFFEE} gr coffee
        {CUP} cup(s)
        {MONEY} USD
    """)


def fill():
    global WATER, MILK, COFFEE, CUP, MONEY

    WATER += int(input("Enter amount of water in stock: "))
    MILK += int(input("Enter amount of milk in stock: "))
    COFFEE += int(input("Enter amount of coffee in stock: "))
    CUP += int(input("Enter amount of cups in stock: "))


def take():
    global WATER, MILK, COFFEE, CUP, MONEY
    MONEY = 0


def buy_coffee(coffee, water, milk, money, coffee_type):
    global WATER, MILK, COFFEE, CUP, MONEY

    requested_cup_num = int(input("How many cups of coffee do you need: "))

    max_cups_water = WATER // water
    max_cups_milk = MILK // milk if milk > 0 else MILK
    max_cups_coffee = COFFEE // coffee
    max_cups = min(max_cups_water, max_cups_coffee, max_cups_milk, CUP)

    if max_cups >= requested_cup_num:
        print("Yes, I can prepare that amount") if max_cups == requested_cup_num else print(
            f"Yes, and {max_cups - requested_cup_num} more cup(s)")
        print(f"Take your {coffee_type}")
        WATER = WATER - water * requested_cup_num
        COFFEE = COFFEE - coffee * requested_cup_num
        MILK = MILK - milk * requested_cup_num
        CUP -= requested_cup_num
        MONEY = MONEY + money * requested_cup_num
    else:
        print(f"No, I can prepare only {max_cups} cup(s)") if max_cups != 0 else print(
            "No, I can not prepare that amount")


def buy():
    coffee_choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if coffee_choice == 1:
        buy_coffee(coffee=16, water=250, milk=0, money=4, coffee_type="espresso")
    elif coffee_choice == 2:
        buy_coffee(coffee=20, water=350, milk=75, money=7, coffee_type="latte")
    elif coffee_choice == 3:
        buy_coffee(coffee=12, water=200, milk=100, money=6, coffee_type="cappuccino")


def main():
    """
    Runs a coffee machine program
    :return: None
    """
    while True:
        choice = input("Write action (buy, fill, take, exit): ")

        if choice == "buy":
            buy()
        elif choice == "fill":
            fill()
        elif choice == "take":
            take()

        show_remaining()

        if choice == "exit":
            break


main()
