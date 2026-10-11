pin = int(input("Enter a 4-digit PIN: "))
num = 1234
count = 3
while count > 1:
    if pin == num:
        print("Your pin is correct")
        break
    else:
        count -= 1
        print("incorrect PIN")
        print(f"Attempts remaining: {count}")
        pin = int(input("Enter a 4-digit PIN again: "))
else:
    print("Locked")
