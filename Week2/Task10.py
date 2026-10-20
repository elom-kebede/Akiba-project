print("Enter 10 numbers: ")
large_num = None
small_num = None
total = 0
count_even = 0
count_odd = 0

for i in range(10):
    num = int(input())
    if num >= 0:
        if large_num is None:
            large_num = num
            small_num = num
        else:
            if num > large_num:
                large_num = num

            if num < small_num:
                small_num = num

        
        
        total += num
        if num % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    else:
        print("please give number greater than zero")
        break

ave = total / 10
if num >0 :
    print(f"Largest number is: {large_num}")
    print(f"Smallest number is: {small_num}")
    print(f"Total sum is: {total}")
    print(f"Average of the number is: {ave}")
    print(f"number of even: {count_even}")
    print(f"number of odd: {count_odd}")
      