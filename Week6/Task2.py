class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must greater than zero.")
        else:
            self.__balance += amount
            print("successfully deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.__balance -= amount
            print("successfully withdrawn:", amount)

    def get_balance(self):
        print(f"Current balance: {self.__balance}")

account1 = BankAccount("Elias", 1000)

account1.deposit(500)
account1.withdraw(200)
account1.get_balance()

