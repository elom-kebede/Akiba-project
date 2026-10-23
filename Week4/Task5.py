balance = float(input("Give the starting balance: "))
transcations = []

total_deposit = 0
total_withdraw = 0
daily_withdraw = 0
daily_limit = 1000

# Record transaction
def rec_transaction(transcation_type, amount, balance_after):
    transcation = {
        "type": transcation_type,
        "amount": amount,
        "balance_after": balance_after
    }
    transcations.append(transcation)



def deposit(amount):
    global balance, total_deposit # tells Python that these variables refer to the variables defined outside the function.
    if amount <= 0:
        print("Error! amount must greater than zero.")
        return

    balance += amount
    total_deposit += amount

    rec_transaction("deposit", amount, balance)

    print(f"Successfully deposited {amount} birr.")

def withdraw(amount):
    global balance, total_withdraw, daily_withdraw
    if amount <= 0:
        print("Error , amount must greater than zero")
        return
    if amount > balance:
        print("Error, insufficient balance")
        return
    
    remaining_limit = daily_limit - daily_withdraw
    if amount > remaining_limit:
        print("Error, daily limit exceed.")
        print(f"Remaining daily limits: {remaining_limit:.2f} birr")
        return

    balance -= amount
    total_withdraw += amount
    daily_withdraw += amount

    rec_transaction("withdraw", amount, balance)
    print(f"Successfully withdrew {amount:.2f} birr.")

def check_balance():
    print(f"Current balance: {balance:.2f} birr.")

# transaction summary
opening_balance = balance # # Save the original opening balance
def trans_summary():
    print("\n=========== TRANSACTION SUMMARY ==========")
    print(f"opening balance: {opening_balance}")
    print(f"Total deposited: {total_deposit}")
    print(f"Total withdrawn: {total_withdraw}")
    print(f"Final balance: {balance}")

    print("\nTransaction History")

    if not transcations:
        print("No successful transactions.")
    else:
        for transaction in transcations:
            print(
                f"Type: {transaction["type"]}, "
                f"Amounts: {transaction["amount"]}, "
                f"Balance after: {transaction["balance_after"]}"
            )
    print("="* 30)

# menu
while True:
    print("\n========== BANK Transaction==========")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        trans_summary()

    elif choice == "5":
        trans_summary()
        print("Thank you for using!")
        break

    else:
        print("Invalid choice. Please select 1-5.")
