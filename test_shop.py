class InsufficientFundsError(Exception):
    pass


def purchase_item(item, items, balance_available):
    if item not in items:
        raise ValueError("Invalid item!")

    item_price = items[item]

    if balance_available >= item_price:
        balance_available -= item_price
        return balance_available
    else:
        raise InsufficientFundsError("You do not have enough funds to complete this transaction.")


def add_funds(amount, balance_available):
    balance_available += amount
    return balance_available


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

            balance_available = purchase_item(choice, items, balance_available)

            print(f"Here's your {choice}!")
            print(f"Remaining balance: £{balance_available}")

        except ValueError as e:
            print(f"Error: {str(e)}. Please try again.")
        except InsufficientFundsError as e:
            print(str(e))
            print("Sorry, you do not have enough funds to complete this transaction.")
            return


# Unit Tests
def test_purchase_item():
    items = {
        "Killian, Love Don't be Shy": 150,
        "Fussy lip gloss": 15,
        "Laura Mercier Setting Powder": 30
    }

    balance_available = 100

    # Valid purchase
    new_balance = purchase_item("Fussy lip gloss", items, balance_available)
    assert new_balance == 85

    # Invalid item
    try:
        purchase_item("Invalid item", items, balance_available)
    except ValueError as e:
        assert str(e) == "Invalid item!"

    # Insufficient funds
    try:
        purchase_item("Killian, Love Don't be Shy", items, balance_available)
    except InsufficientFundsError as e:
        assert str(e) == "You do not have enough funds to complete this transaction."


def test_add_funds():
    balance_available = 100

    new_balance = add_funds(50, balance_available)
    assert new_balance == 150


def test_shop():
    # Simulating user input during testing
    input_values = ["Fussy lip gloss", "exit"]
    input_index = 0

    def mock_input(prompt):
        nonlocal input_index
        input_index += 1
        return input_values[input_index - 1]

    # Valid purchase
    shop()
    assert input_index == 2

    # Invalid item
    input_values = ["Invalid item", "exit"]
    input_index = 0
    shop()
    assert input_index == 2

    # Insufficient funds
    input_values = ["Killian, Love Don't be Shy", "no"]
    input_index = 0
    shop()
    assert input_index == 2


# Run the unit tests
test_purchase_item()
test_add_funds()
test_shop()
