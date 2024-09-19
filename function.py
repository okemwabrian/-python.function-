def calculate_discount(price, discount_percent):
    # Apply discount only if it's 20% or higher
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

# Prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(price, discount_percent)

# Print the final price or the original price
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {price:.2f}")
