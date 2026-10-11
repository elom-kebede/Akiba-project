num = int(input("Enter a positive number: "))
i = 1
even = 0
odd = 0
sum = 0

while i <= num:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1
    
    sum+=i
    i+=1
print(f"even {even}")
print(f"odd {odd}")
print(f"sum of numbers is {sum}")
