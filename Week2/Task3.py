# This program checks if a number is prime or not
num = int(input("enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num == 2):
            print(f"{num} is a prime number")
            break
        elif (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
            
else:
    print(f"{num} is not a prime number")