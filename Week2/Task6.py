starting_num = int(input("Enter the starting number greater than 0: "))
ending_num = int(input("Enter the ending number less or equal t0 100: "))

while starting_num <= ending_num:
    if starting_num % 3 == 0 and starting_num % 5 ==0:
            print("FizzBuzz")
            starting_num += 1
    elif starting_num % 3 == 0:
        print("Fizz")
        starting_num += 1
    elif starting_num % 5 == 0:
        print("Buzz")
        starting_num += 1
    
    else:
        print(starting_num)
        starting_num += 1