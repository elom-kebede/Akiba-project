num = int(input("Enter a number: "))
if num % 2 == 0:
    if num > 0:
        print(f"{num} is a positive even number.")
    elif num < 0:
        print(f"{num} is a negative even number.")
    else:
        print(f"The number is zero, which is considered even.")
else:
    if num > 0:
        print(f"{num} is a positive odd number.")
    else:
        print(f"{num} is a negative odd number.")
    