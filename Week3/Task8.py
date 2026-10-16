unit = int(input("Enter the unit: " ))
#function for validate
def unit_validate(unit):
    if unit <= 0:
        return False
    else: 
        return True

# function to calculate tier one
def calculate_tier_one(unit):
    if unit <= 50:
        res = unit * 0.50
    else:
        res = 50 * 0.50
    return res

# function to calculate tier one
def calculate_tier_two(unit):
    if unit <= 50:
        return 0
    elif unit <= 150:
        res = (unit - 50) * 0.75
    else:
        res = 100 * 0.75
    return res

# function to calculate tier three
def calculate_tier_three(unit):
    if unit <= 150:
        return 0
    else:
        return (unit - 150) * 1.20

# to check
# print(calculate_tier_one(unit))
# print(calculate_tier_two(unit))
# print(calculate_tier_three(unit))

# function for the total bill
def total_bill(service_fee = 10):
    total = calculate_tier_one(unit) + calculate_tier_two(unit) + calculate_tier_three(unit) + service_fee
    return total

# function for bill_summary
def bill_summary(service_fee = 10):
    print("\n====== BILL SUMMARY======\n")
    print(f"The unit is: {unit}")
    print(f"First tier charge: {calculate_tier_one(unit)}")
    print(f"Second tier charge: {calculate_tier_two(unit)}")
    print(f"Third tier charge: {calculate_tier_three(unit)}")
    print(f"Service fee: {service_fee}")
    print()
    print(f"Total bill: {total_bill(service_fee)}")
    print("="*30)

if unit_validate(unit):
    bill_summary()
else:
    print("Invalid input! a unit can't be negative or zero")

    
    
    
