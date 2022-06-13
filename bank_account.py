# Pin code - hint: the year

def account():
    name = "Dana"
    pin = 2022
    attempt = 1
    left = 2
    balance = 2000

    print(f"You have 3 attempts to enter the right pin code.")

    try:
        for i in range(3):
            guess = int(input("Enter Pin Code: "))

            if guess == pin:
                print(f"Welcome {name}!")
                chose = int(input(f"Press 1 for balance or 2 for withdrawal: "))

                if chose == 1:
                    balance_info(balance)
                    break
                elif chose == 2:
                    withdraw_info(balance)
                    break
                else:
                    print("Please take the card!")
                    break

            elif guess != pin:
                print(f"That was your {attempt} wrong attempt!")
                print(f"You have {left} attempts left.")
                attempt += 1
                left -= 1

            if attempt == 4:
                print("Your card was blocked!")
                break

    except ValueError:
        # Print the error message
        print("Please take the card!")


def balance_info(balance):

    print(f"Your balance is {balance}€")
    wd = input("Do you want to withdraw? 'y' for yes ")

    if wd == "y":
        withdraw_info(balance)
    else:
        print("Please take the card!")


def withdraw_info(balance):
    money = int(input("How much money do you want to withdraw? "))

    if money <= balance:
        balance -= money
        print(f"\nWithdrawal accepted!\nYou withdraw {money}€.\nYour new balance is {balance}€!")

    else:
        print(f"The balance is too low. You have {balance}€.")
        print("Please take the card!")


account()
