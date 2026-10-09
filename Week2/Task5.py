# sum of digits of a number
num = (input("Enter a number: "))
sum = 0
if num.isdigit():
    for n in num:
      sum += int(n)
    print(f"The sum of digits of {num} is: {sum}")
     
     
else:
    print("Please enter a valid number.")
       

       