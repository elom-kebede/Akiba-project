items = [
    {"name": "Notebook", "price": 0, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]
tax_rate = float(input("Enter tax rate (%): ")) / 100

# checking validity
def check_valid(items):
    if tax_rate <= 0:
        return False
    for item in items:
        if item["price"] <= 0 or item["quantity"] <= 0:
           return False
        
    else:
        return True

# calcualte totla cost
def calculate_subtotal(items):
    subtotal = 0
    for i in range(len(items)):
        subtotal += items[i]["price"] * items[i]["quantity"]
        
    return subtotal

subtotal = calculate_subtotal(items)

# calculate discount
def calculate_discount(subtotal):
    if subtotal < 1000:
        
        ans =0
    elif subtotal < 3000:
        ans = subtotal * 0.05
    else:
        ans = subtotal * 0.1
    return ans

# calculate the tax
def calculate_tax(subtotal, tax_rate):
    discount = calculate_discount(subtotal)
    tax = (subtotal-discount) * tax_rate
    return tax


def final_amount():
    discount = calculate_discount(subtotal)
    tax = calculate_tax(subtotal,tax_rate)
    amount = subtotal - discount + tax
    return amount

# generate the receipt
def generate_receipt(tax_rate):
    print("\n====== RECEIPT ======\n")
    print(f"{'Subtotal':<25}{subtotal}")
    print(f"{'Discount':<25}{calculate_discount(subtotal)}")
    print(f"{'Tax':<25}{calculate_tax(subtotal, tax_rate)}")
    print(f"{'Final amount':<25}{final_amount()}")
    print("=" *30)

if check_valid(items): 
   generate_receipt(tax_rate)

else:
    print("Invalid , price, quantity and tax must greater than zero")