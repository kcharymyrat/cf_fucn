# Stage 3

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


def buy_espresso():
    global WATER, MILK, COFFEE, CUP, MONEY

    esp_coffee = 16
    esp_water = 250
    esp_money = 4

    requested_cup_num = int(input("How many cups of coffee do you need: "))

    max_cups_water = WATER // esp_water
    # max_cups_milk = milk_stock // MILK
    max_cups_coffee = COFFEE // esp_coffee
    max_cups = min(max_cups_water, max_cups_coffee, CUP)

    if max_cups >= requested_cup_num:
        print("Yes, I can prepare that amount") if max_cups == requested_cup_num else print(
            f"Yes, and {max_cups - requested_cup_num} more cup(s)")
    else:
        print(f"No, I can prepare only {max_cups} cup(s)") if max_cups != 0 else print(
            "No, I can not prepare that amount")

    if esp_coffee <= COFFEE and esp_water <= WATER:

        WATER -= esp_water
        COFFEE -= esp_coffee
        CUP -= 1
        MONEY += esp_money
    else:
        print("Sorry, but there is not enough ingredients")


def buy_latte():
    global WATER, MILK, COFFEE, CUP, MONEY

    latte_coffee = 20
    latte_water = 350
    latte_milk = 75
    latte_money = 7

    requested_cup_num = int(input("How many cups of coffee do you need: "))

    max_cups_water = WATER // latte_water
    max_cups_milk = MILK // latte_milk
    max_cups_coffee = COFFEE // latte_coffee
    max_cups = min(max_cups_water, max_cups_coffee, max_cups_milk, CUP)

    if max_cups >= requested_cup_num:
        print("Yes, I can prepare that amount") if max_cups == requested_cup_num else print(
            f"Yes, and {max_cups - requested_cup_num} more cup(s)")
    else:
        print(f"No, I can prepare only {max_cups} cup(s)") if max_cups != 0 else print(
            "No, I can not prepare that amount")

    if latte_coffee * requested_cup_num <= COFFEE and latte_water * requested_cup_num <= WATER and latte_milk * requested_cup_num <= MILK:

        WATER -= latte_water
        COFFEE -= latte_coffee
        MILK -= latte_milk
        CUP -= 1
        MONEY += latte_money
    else:
        print("Sorry, but there is not enough ingredients")


def buy_cappuccino():
    global WATER, MILK, COFFEE, CUP, MONEY

    cap_coffee = 12
    cap_water = 200
    cap_milk = 100
    cap_money = 6

    requested_cup_num = int(input("How many cups of coffee do you need: "))

    max_cups_water = WATER // cap_water
    max_cups_milk = MILK // cap_milk
    max_cups_coffee = COFFEE // cap_coffee
    max_cups = min(max_cups_water, max_cups_coffee, max_cups_milk, CUP)

    if max_cups >= requested_cup_num:
        print("Yes, I can prepare that amount") if max_cups == requested_cup_num else print(
            f"Yes, and {max_cups - requested_cup_num} more cup(s)")
    else:
        print(f"No, I can prepare only {max_cups} cup(s)") if max_cups != 0 else print(
            "No, I can not prepare that amount")

    if cap_coffee <= COFFEE and cap_water <= WATER and cap_milk <= MILK:
        print("Take your capuccino")
        WATER -= cap_water
        COFFEE -= cap_coffee
        MILK -= cap_milk
        CUP -= 1
        MONEY += cap_money
    else:
        print("Sorry, but there is not enough ingredients")


def buy():
    global WATER, MILK, COFFEE, CUP, MONEY
    coffee_choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:"))
    if coffee_choice == 1:
        buy_espresso()
    elif coffee_choice == 2:
        buy_latte()
    elif coffee_choice == 3:
        buy_cappuccino()


def main():
    global WATER, MILK, COFFEE, CUP, MONEY
    while True:

        choice = input("Write action (buy, fill, take)")

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
