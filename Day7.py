def calculate_total_price(price, tax_rate):
    # Calculate the tax amount
    tax_amount = price * tax_rate
    
    # Calculate the total final price
    total = price + tax_amount
    
    return total

# Example usage:
final_bill = calculate_total_price(100, 0.05)
print(final_bill)
