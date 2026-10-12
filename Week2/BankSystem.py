def menu():
      print(f"{y} AKIBA BANK {y}")
      print("1. Check Balance")
      print("2. Deposit Money")
      print("3. Withdraw Money")
      print("4. Exit")
y = "="*4
balance = 1000
isTrue = True
pin = 1234
i = 3
while i>0: # this is for pin check
    code = int(input("Enter your pin: "))
    if pin == code:
        while isTrue:
            menu()
            num = input("Enter a number: ")
            if num == "1":
                print(balance)
            elif num == "2":
                deposit = int(input("Enter deposit amount: "))
                if(deposit > 0):
                   balance+=deposit
                   print("Deposit successful")
                   print(f"Your new balance is: {balance}")
                else:
                    print("0 and negative deposit is not allowed")
            elif num == "3":
                withdraw = int(input("Enter withdrawal amount: "))
                if withdraw > balance:
                    print("insufficient balance")
                else:
                    balance-= withdraw
                    print("Withdrawal successful!")
                    print(f"Your new balance is: {balance}")
            elif num == "4":
                print("Thank you for using Akiba Bank!\nGoodbye!")
                isTrue = False
                break
            else:
                print("Invalid option")
                print("Please choose a valid option")
        else:
            i-=1
            print(f"Your pin is incorrect! {i} Attempt left")
            
else:
    print("locked")





   
