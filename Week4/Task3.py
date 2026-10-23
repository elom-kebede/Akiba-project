number = int(input("Enter number: "))

#checking prime number
def is_prime(number):
    if number > 0:
        if number == 1:
            return "not prime"
        for i in range(2,number):
            if number % i == 0:
                return "not prime"
            else:
                return "prime"
    else:
        return "please give a number greate than zero"
    
# get divisor
def get_divisor(number):
    div = []
    for i in range(1,number+1):
        if number % i == 0:
            div.append(i)
    return div
# print(get_divisor(number))

# sum of digit
def sum_of_digits(number):
    sum = 0
    for i in range(number+1):
        sum += i
    return sum
# print(sum_of_digits(number))

# reverse number 
def reverse_number(number):
    num = str(number)
    rnum = ""
    for i in num[::-1]:
        rnum+=i
        
    
    return rnum
        
        
# complete analysis
def analyze_number(number):
    isprime = is_prime(number)
    divisors = get_divisor(number)
    sumdigit = sum_of_digits(number)
    reverse = reverse_number(number)
    print("\n=========analysis========")
    print(f"The number is: {isprime}")
    print(f"The divisors are {divisors}")
    print(f"The sum of the digits {sumdigit}")
    print(f"The reverse number is: {reverse}")

analyze_number(number)
