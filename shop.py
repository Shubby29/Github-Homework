class InsufficientFundsError(Exception):
    pass


def shop():
    items = {
        "Killian, Love Don't be Shy": 150,
        "Fussy lip gloss": 15,
        "Laura Mercier Setting Powder": 30,
        "Nars Foundation": 36,
        "Charlotte Tilbury Faux Filter": 39,
        "Kevyn Aucoin enhancer": 38
    }

    balance_available = 100

    print("Welcome to the shop!")
    print("Here are the items and their prices:")
    for item, price in items.items():
        print(f"{item}: £{price}")

    while True:
        try:
            choice = input("Please enter the item you wish to purchase (or 'exit' to leave the shop): ")

            if choice == "exit":
                print("Thank you for visiting the shop! We hope to see you soon")
                return

            if choice not in items:
                raise ValueError("Invalid item!")

            item_price = items[choice]

            if balance_available >= item_price:
                print(f"Here's your {choice}!")
                balance_available -= item_price
                print(f"Remaining balance: £{balance_available}")
            else:
                print("You do not have enough money to purchase this item.")
                alternative_payment = input("Do you wish to use a different account to fund this purchase? (yes/no): ")

                if alternative_payment.lower() == "yes":
                    extra_funds = float(input("Enter the amount: "))
                    balance_available += extra_funds
                    print(f"Updated balance: £{balance_available}")
                elif alternative_payment.lower() == "no":
                    raise InsufficientFundsError("You do not have enough funds to complete this transaction.")
                else:
                    raise ValueError("Invalid input!")

        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")
        except InsufficientFundsError as e:
            print(str(e))
            print("Sorry, you do not have enough funds to complete this transaction.")
            return


try:
    shop()
except KeyboardInterrupt:
    print("\nProgram terminated.")
